---
title: "Kiểm tra dữ liệu chứng chỉ trong file CSV bằng Python: ngày hợp lệ và trạng thái hiệu lực"
slug: "kim-tra-d-liu-chng-ch-trong-file-csv-bng-python-ngy-hp-l-v-trng-thi-hiu-lc"
author: "nghiepvuvietnam"
source: "devto_python"
published: "Tue, 17 Nov 2026 15:35:04 +0000"
description: "Khi quản lý một danh sách giấy chứng nhận hay chứng chỉ trong file CSV, lỗi hay gặp nhất không nằm ở logic phức tạp mà ở dữ liệu: ô ngày để trống, ngày không..."
keywords: "het, loi, han, date, chi, dong, cap, tra"
generated: "2026-11-17T15:45:53.610262"
---

# Kiểm tra dữ liệu chứng chỉ trong file CSV bằng Python: ngày hợp lệ và trạng thái hiệu lực

## Overview

Khi quản lý một danh sách giấy chứng nhận hay chứng chỉ trong file CSV, lỗi hay gặp nhất không nằm ở logic phức tạp mà ở dữ liệu: ô ngày để trống, ngày không tồn tại, ngày hết hạn đứng trước ngày cấp. Bài này viết một đoạn Python nhỏ, chỉ dùng thư viện chuẩn, để đọc CSV, kiểm tra từng dòng và phân loại trạng thái hiệu lực. Mã đã chạy thử trên Python 3.12. Bài toán Mỗi dòng gồm họ tên, tên chứng chỉ, ngày cấp và ngày hết hạn (có thể để trống nếu chứng chỉ không ghi thời hạn). Ta muốn: Đọc được dòng hợp lệ thành đối tượng có kiểu rõ ràng. Gom riêng các dòng lỗi kèm số dòng để người nhập sửa lại. Phân loại: không thời hạn, còn hạn, sắp hết hạn, đã hết hạn. Mã nguồn import csv , io from dataclasses import dataclass from datetime import date , datetime DATA = """ho_ten,ten_chung_chi,ngay_cap,ngay_het_han An,Chung chi A,2023-03-10,2026-03-10 Binh,Chung chi B,2024-05-01, Chi,Chung chi A,2022-12-31,2025-12-31 Dung,Chung chi C,2025-02-30,2028-02-28 Hoa,Chung chi B,2026-01-15,2025-01-15 """ @dataclass class HoSo : ho_ten : str chung_chi : str ngay_cap : date ngay_het_han : date | None def doc_ngay ( s ) : s = s . strip ( ) return datetime . strptime ( s , "%Y-%m-%d" ) . date ( ) if s else None def doc_ho_so ( text ) : hop_le , loi = [ ] , [ ] for dong , r in enumerate ( csv . DictReader ( io . StringIO ( text ) ) , start = 2 ) : try : cap = doc_ngay ( r [ "ngay_cap" ] ) het = doc_ngay ( r [ "ngay_het_han" ] ) if het and het < cap : raise ValueError ( "ngay het han truoc ngay cap" ) hop_le . append ( HoSo ( r [ "ho_ten" ] , r [ "ten_chung_chi" ] , cap , het ) ) except ValueError as e : loi . append ( ( dong , r [ "ho_ten" ] , str ( e ) ) ) return hop_le , loi def trang_thai ( h , hom_nay , sap_het = 90 ) : if h . ngay_het_han is None : return "khong thoi han" con = ( h . ngay_het_han - hom_nay ) . days if con < 0 : return "da het han" return "sap het han" if con <= sap_het else "con han" if __name__ == "__main__" : hom_nay = date ( 2026 , 11 , 18 ) ds , loi = doc_ho_so ( DATA ) for h in ds : print ( h . ho_ten , "-" , trang_thai ( h , hom_nay ) ) for dong , ten , msg in loi : print ( "LOI dong" , dong , ten , ":" , msg ) Giải thích dataclass. HoSo giữ dữ liệu một dòng. Ngày hết hạn có kiểu date | None để thể hiện chứng chỉ không ghi thời hạn, thay vì dùng chuỗi rỗng. Bắt lỗi theo từng dòng. datetime.strptime tự từ chối ngày không tồn tại như 30/02, nên ta không cần viết thêm luật kiểm tra lịch. Lỗi được ghi vào danh sách loi kèm số dòng (bắt đầu từ 2 vì dòng 1 là tiêu đề), chương trình vẫn chạy tiếp các dòng còn lại. Luật nghiệp vụ. Điều kiện het < cap bắt trường hợp ngày hết hạn đứng trước ngày cấp, thường do nhập nhầm. Truyền ngày hiện tại vào hàm. trang_thai nhận hom_nay làm tham số thay vì gọi date.today() bên trong. Nhờ vậy kết quả lặp lại được và dễ viết kiểm thử. Kết quả chạy thử Với dữ liệu mẫu và ngày tham chiếu 18/11/2026: An - da het han Binh - khong thoi han Chi - da het han LOI dong 5 Dung : day is out of range for month LOI dong 6 Hoa : ngay het han truoc ngay cap Hai dòng lỗi được tách riêng, ba dòng hợp lệ được phân loại đúng. Mở rộng Xuất danh sách lỗi ra file để gửi lại người nhập. Đổi ngưỡng sap_het theo từng loại giấy tờ. Thêm kiểm thử với unittest , truyền nhiều giá trị hom_nay để kiểm tra các mốc biên. Nếu dữ liệu lớn, chuyển sang pandas, nhưng phần luật kiểm tra vẫn giữ như trên. Dữ liệu trong bài là dữ liệu mẫu tự tạo, không phải hồ sơ thật.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nghiepvuvietnam/kiem-tra-du-lieu-chung-chi-trong-file-csv-bang-python-ngay-hop-le-va-trang-thai-hieu-luc-2oil

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
