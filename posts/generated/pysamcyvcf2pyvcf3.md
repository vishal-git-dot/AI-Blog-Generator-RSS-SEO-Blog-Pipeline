---
title: "pysam、cyvcf2、PyVCF3 性能對比與應用"
slug: "pysamcyvcf2pyvcf3"
author: "JH5"
source: "devto_python"
published: "Sat, 13 Jun 2026 04:07:32 +0000"
description: "pysam、cyvcf2、PyVCF3 性能對比與應用 在生物資訊的世界裡，處理基因組變異數據是在日常不過的工作，從最入門的PyVCF3 再到 pysam 除了可以除了vcf外，還可以一並處理GATK前後處理，再到 cyvcf2 可以處理大型WGS檔案以及批次同時處理多個VCF檔，到底要怎麼選？ UpdatedM..."
keywords: "vcf, pysam, print, variant, record, import, variantfile, qual"
generated: "2026-06-13T04:19:15.384458"
---

# pysam、cyvcf2、PyVCF3 性能對比與應用

## Overview

pysam、cyvcf2、PyVCF3 性能對比與應用 在生物資訊的世界裡，處理基因組變異數據是在日常不過的工作，從最入門的PyVCF3 再到 pysam 除了可以除了vcf外，還可以一並處理GATK前後處理，再到 cyvcf2 可以處理大型WGS檔案以及批次同時處理多個VCF檔，到底要怎麼選？ UpdatedMarch 24, 2026•3 min read J JhihHao Wu ** 近期研究重點包含 AI Agent 的供應鏈攻擊、PII 偵測模型評估，以及醫療 AI 在臨床流程中的安全落地。 在這裡，我分享深度技術實測報告（如 NVIDIA NeMo, WildGuard）與職場技術成長心得，致力於在 AI 浪潮中打造具備資安韌性的解決方案。 On this page pysam、cyvcf2、PyVCF3 性能對比與應用1. pysam (0.23.3)2. cyvcf2 (0.31.4)3. PyVCF3 (1.0.3)Case1. 過濾高品質變異（QUAL≥30, DP≥20）Case2. 變異類型統計Case 3. 平行處理多個 VCFCase4. 區域查詢（需要 .tbi 索引）Case5. 合併多個樣本的 VCF pysam、cyvcf2、PyVCF3 性能對比與應用 BAM Viewer 在生物資訊的世界裡，處理基因組變異數據是在日常不過的工作，從最入門的 PyVCF3 再到 pysam 除了可以除了vcf外，還可以一並處理GATK前後處理，再到 cyvcf2 可以處理大型WGS檔案以及批次同時處理多個VCF檔，到底要怎麼選？ 1. pysam (0.23.3) 這是最一開始Agent推薦給我的tools，支援常見的格式檔案，SAM、BAM、CRAM、VCF、BCF，也可以直接呼叫 samtools/bcftools ，除了新手友善之外，我覺得CP值也滿高的，不過在讀取WGS時就會有一些小問題，後面再補充。 import pysam vcf = pysam . VariantFile ( " output.vcf.gz " ) for variant in vcf : print ( f " { variant . chrom } : { variant . pos } " f " { variant . ref } → { variant . alts [ 0 ] } " ) print ( f " QUAL: { variant . qual } " ) print ( f " DP: { variant . info . get ( ' DP ' , ' N/A ' ) } " ) 2. cyvcf2 (0.31.4) 架構：Python API → Cython → htslib C lib 這樣標準的python加速底子，好像要不快都很難，特別是他有針對VCF內的INFO字串做了優化，如果你常常需要載入WGS百萬筆的variants，可以選用cyvcf2 來避免懷疑人生ＸＤ import cyvcf2 vcf = cyvcf2 . VCF ( " population.vcf.gz " ) # 快速統計等位基因頻率 allele_freqs = [] for variant in vcf : if ' AF ' in variant . INFO : allele_freqs . append ( variant . INFO [ ' AF ' ][ 0 ]) print ( f " 平均 AF: { sum ( allele_freqs ) / len ( allele_freqs ) : . 4 f } " ) 3. PyVCF3 (1.0.3) 都2026年了，如果有LLM 推薦這個工具給你，我建議你退訂或移除它。 Case1. 過濾高品質變異（QUAL≥30, DP≥20） import pysam def filter_high_quality_variants ( input_vcf , output_vcf ): vcf_in = pysam . VariantFile ( input_vcf ) vcf_out = pysam . VariantFile ( output_vcf , ' w ' , header = vcf_in . header ) stats = { ' total ' : 0 , ' passed ' : 0 } for record in vcf_in : stats [ ' total ' ] += 1 # 過濾條件 qual_pass = record . qual is not None and record . qual >= 30 depth_pass = ' DP ' in record . info and record . info [ ' DP ' ] >= 20 if qual_pass and depth_pass : vcf_out . write ( record ) stats [ ' passed ' ] += 1 vcf_in . close () vcf_out . close () # 輸出統計 pass_rate = 100 * stats [ ' passed ' ] / stats [ ' total ' ] print ( f " 結果統計: " ) print ( f " 總變異數: { stats [ ' total ' ] } " ) print ( f " 高品質變異: { stats [ ' passed ' ] } ( { pass_rate : . 1 f } %) " ) return stats # 執行 results = filter_high_quality_variants ( " output.vcf.gz " , " filtered.vcf " ) Case2. 變異類型統計 import pysam from collections import Counter def analyze_variant_types ( vcf_file ): """ 統計 SNP、INS、DEL 比例 """ vcf = pysam . VariantFile ( vcf_file ) variant_types = Counter () for record in vcf : ref_len = len ( record . ref ) alt_len = len ( record . alts [ 0 ]) if record . alts else 0 if ref_len == alt_len == 1 : variant_types [ ' SNP ' ] += 1 elif ref_len < alt_len : variant_types [ ' INDEL (INS) ' ] += 1 elif ref_len > alt_len : variant_types [ ' INDEL (DEL) ' ] += 1 else : variant_types [ ' COMPLEX ' ] += 1 vcf . close () # 可視化結果 total = sum ( variant_types . values ()) print ( f " \n . 變異類型分佈 (共 { total } 個): " ) print ( " ─ " * 40 ) for vtype , count in sorted ( variant_types . items (), key = lambda x : x [ 1 ], reverse = True ): percentage = 100 * count / total bar = " █ " * int ( percentage / 2 ) print ( f " { vtype : 15 } { count : 4 } ( { percentage : 5.1 f } %) { bar } " ) return dict ( variant_types ) # 執行 types = analyze_variant_types ( " output.vcf.gz " ) 預期應該可以看到類似的結果 SNP 250 ( 86.8%) ███████████████████████████████████ INDEL (INS) 18 ( 6.2%) ███ INDEL (DEL) 15 ( 5.2%) ██ COMPLEX 5 ( 1.7%) █ Case 3. 平行處理多個 VCF from multiprocessing import Pool import pysam def process_single_vcf ( vcf_file ): """ 單個 VCF 的處理 """ vcf = pysam . VariantFile ( vcf_file ) high_quality = sum ( 1 for rec in vcf if rec . qual and rec . qual >= 30 ) return { ' file ' : vcf_file , ' high_quality ' : high_quality } def batch_process_vcfs ( vcf_files , num_processes = 4 ): """ 批量處理多個 VCF """ print ( f " 🚀 使用 { num_processes } 個process平行處理... " ) with Pool ( processes = num_processes ) as pool : results = pool . map ( process_single_vcf , vcf_files ) # 彙總結果 print ( " \n Batch分析結果: " ) total_high_quality = 0 for result in results : print ( f " { result [ ' file ' ] } : { result [ ' high_quality ' ] } 高品質變異 " ) total_high_quality += result [ ' high_quality ' ] print ( f " \n 總計: { total_high_quality } 高品質變異 " ) # 使用 vcf_list = [ " sample1.vcf.gz " , " sample2.vcf.gz " , " sample3.vcf.gz " ] batch_process_vcfs ( vcf_list , num_processes = 4 ) Case4. 區域查詢（需要 .tbi 索引） import pysam vcf = pysam.VariantFile("indexed.vcf.gz") # 只查詢特定區域，快速過濾 for variant in vcf.fetch("chr1", 1000000, 2000000): print(variant) Case5. 合併多個樣本的 VCF import pysam vcfs = [ pysam . VariantFile ( "sample1.vcf.gz" ), pysam . VariantFile ( "sample2.vcf.gz" ), ] merged = pysam . VariantFile ( "merged.vcf" , 'w' , header = vcfs [ 0 ]. header ) for vcf in vcfs: for record in vcf: merged . write ( record ) merged . close () 除了一些應用的案例，效能上實測的結果 cyvcf2 再載入WES的vcf大多1–2秒就可以完成，大一點的WGS左右的vcf檔案約落在3–4 mins，pysam WES 左右大約20秒以內，WGS的看心情ＸＤ 最久有遇到大於5 mins ，PyVCF3 就不提了ＸＤ 簡單的結論就是 需要處理 BAM 檔案？ → pysam 只處理 VCF，要最快？ → cyvcf2 學習 VCF 格式？ → pysam BTW，如果有遇到 libhts.so.3: cannot open shared object file ，記得要 sudo apt-get install libhts-dev 或是直接 pip install --force-reinstall cyvcf2 # bioinformatics # genomics # python **2 views

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jh5_pulse/pysam-cyvcf2-pyvcf3-xing-neng-dui-bi-yu-ying-yong-43pa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
