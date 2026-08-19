---
title: "Tôi đã dùng AI viết code được 8 tháng, và đây là những gì tôi thực sự nghĩ"
slug: "ti-dng-ai-vit-code-c-8-thng-v-y-l-nhng-g-ti-thc-s-ngh"
author: "TOT"
source: "devto_webdev"
published: "Wed, 19 Aug 2026 06:45:42 +0000"
description: "Có một giai đoạn tôi gõ prompt cho AI xong là copy paste thẳng vào project, không đọc kỹ. Code chạy, demo mượt, sếp gật đầu. Rồi hai tuần sau, một bug produc..."
keywords: "code, khi, review, cho, sau, logic, trong, prompt"
generated: "2026-08-19T06:52:53.079961"
---

# Tôi đã dùng AI viết code được 8 tháng, và đây là những gì tôi thực sự nghĩ

## Overview

Có một giai đoạn tôi gõ prompt cho AI xong là copy paste thẳng vào project, không đọc kỹ. Code chạy, demo mượt, sếp gật đầu. Rồi hai tuần sau, một bug production khiến tôi mất cả buổi tối để tìm ra nguyên nhân: một điều kiện biên mà AI "quên" xử lý, vì tôi chưa bao giờ nói rõ nó cho AI biết. Từ đó tôi bắt đầu dùng AI khác đi. Không phải bỏ, mà là dùng có ý thức hơn. Bài này không phải hướng dẫn kỹ thuật, chỉ là vài điều tôi rút ra sau một thời gian đủ dài để hết hưng phấn ban đầu. AI không lười, nó chỉ không biết nó đang thiếu gì Điều làm tôi bất ngờ nhất không phải là AI viết sai, mà là nó viết đúng cú pháp một cách rất tự tin, kể cả khi logic sai hoàn toàn. Không có tín hiệu cảnh báo nào cả. Một hàm tính discount chạy êm ru cho đến khi có ai đó nhập percent âm. Tôi dần hiểu ra: mô hình không "hiểu" nghiệp vụ của tôi, nó chỉ dự đoán phần code có khả năng xuất hiện tiếp theo dựa trên những gì tôi đã mô tả. Nếu tôi mô tả sơ sài, nó lấp đầy khoảng trống bằng giả định riêng, và giả định đó không phải lúc nào cũng đúng với hệ thống của tôi. Vậy nên giờ trước khi để AI viết bất cứ thứ gì động đến logic quan trọng, tôi tự hỏi: nếu một dev mới vào công ty, chưa biết gì về codebase, đọc đúng những gì tôi vừa gõ, họ có viết ra thứ tôi muốn không? Nếu câu trả lời là không chắc, prompt của tôi chưa đủ. Cái bẫy dễ mắc nhất: để AI viết cả một tính năng trong một lần Lúc mới dùng, tôi hay yêu cầu kiểu "viết giúp mình chức năng đăng nhập hoàn chỉnh". Kết quả thường thiếu một trong các phần: hash password đúng chuẩn, xử lý token hết hạn, hoặc validate input. Không phải vì AI dở, mà vì yêu cầu quá rộng, AI phải tự chọn cái gì quan trọng, và lựa chọn đó không phải lúc nào cũng trùng với thứ tôi cần. Cách đỡ hơn nhiều là chia nhỏ. Từng phần một, review từng phần trước khi ghép lại. Chậm hơn so với việc nhận nguyên một khối code trong 10 giây, nhưng tổng thời gian debug sau đó giảm hẳn. Review code AI như review code một bạn junior mới vào team Đây là thay đổi tư duy lớn nhất của tôi. AI không biết lịch sử tại sao một đoạn logic cũ trong project được viết kỳ lạ như vậy, không biết những case đặc biệt mà team đã từng gặp và fix trước đó. Nó chỉ thấy được đúng phần context tôi đưa vào prompt. Vậy nên tôi review code AI đúng như review code của một bạn mới, kể cả khi code đó "nhìn có vẻ ổn". Chạy test, thử vài edge case, đọc kỹ phần xử lý lỗi. Với những phần động đến bảo mật hoặc dữ liệu tiền bạc, tôi luôn tự tay viết lại phần validate, thay vì tin hoàn toàn vào AI. Có một dạo tôi cũng tò mò thử qua lại nhiều công cụ khác nhau xem cái nào hợp với workflow của mình, và tình cờ đọc được một bài tổng hợp khá chi tiết về ai viết code , so sánh điểm mạnh yếu của từng loại theo nhu cầu sử dụng thực tế, đỡ phải tự cài rồi test từng cái một như tôi đã làm lúc đầu. Điều tôi vẫn giữ lại sau 8 tháng Tôi không bỏ AI, ngược lại còn dùng nhiều hơn cho những việc lặp lại: viết boilerplate, sinh unit test cho các case cơ bản, giải thích một đoạn code cũ không ai còn nhớ logic. Những việc đó AI làm nhanh và khá ổn. Nhưng với những quyết định ảnh hưởng đến kiến trúc, hoặc code chạm vào dữ liệu nhạy cảm, tôi vẫn tự viết hoặc ít nhất tự đọc lại từng dòng trước khi merge. AI với tôi bây giờ giống một đồng nghiệp làm việc nhanh nhưng chưa quen dự án, hữu ích thật, chỉ là không thể giao việc rồi quay lưng đi luôn được. Bạn nào cũng đang dùng AI để code hằng ngày, mình tò mò cách các bạn kiểm soát chất lượng ra sao, đặc biệt là phần review. Để lại comment nhé.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tot2019/toi-da-dung-ai-viet-code-duoc-8-thang-va-day-la-nhung-gi-toi-thuc-su-nghi-3l32

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
