# Architectures

Một LLM được cấu thành bởi các thành phần:

- Một Tokenizer chuyển đổi Text thành các Tokens. Mỗi Token là một số từ $1 \to K$ tương ứng với một Word, Sub-word hay Character nào đó

- Một Deep Network Interpret những Token này với 4 kiểu Architecture phổ biến nhất:

  - Encoder-Decoder (kiến trúc Transformer ban đầu)
  - Encoder-only (chỉ Encode Text thành Embedding)
  - Decoder-only (có thể sản sinh ra Text)
  - Sequence Models (RNNs, LSTM, GRU ...)

- Một Detokenizer chuyển đổi Tokens lại thành Text

Vậy, quá trình Tokenization và Detokenization diễn ra như thế nào?

Cách đơn giản nhất là sử dụng Character-level Tokenizer với mỗi Input Character $c_1, ..., c_N$ có thể được quy đổi thành một Character-level Embedding $e_1, ..., e_256$ tương ứng. Sau đó, các Embedding có thể trở thành Input cho Deep Network để tạo ra Output là một Detokenized Character được Sample từ Distribution của tất cả các Character. Tuy nhiên, một vấn đề lớn của dạng Tokenizer này là Sequence cần được xử lý sẽ rất dài và các LLM vẫn còn gặp nhiều khó khăn trong việc này.

Thay vì thế, một dạng Tokenization khác đang được rộng rãi đó là Byte-Pair Encoding (BPE). BPE hoạt động bằng cách lựa chọn một kho từ vựng $V$ với $N$ phần tử, chia nhỏ Input D ra thành từng Character Token và cứ thế Merge dần những Token Pair xuất hiện nhiều lần nhất lại với nhau để tạo ra các Token mới là các Sub-word cho tới khi $V$ đạt tới kích thước $N$.

Sau khi đã được Tokenize và Embed, Input Embedding sẽ được Feed vào một Deep Network với các kiểu Architecture như trên. Network này sau đó sẽ sản sinh ra các Output Feature có cùng Dimension với Input và là các Distributions / Logits lên tất cả các Token:

- Encoder-Decoder:

  - Là dạng Transformer ban đầu được thiết kế cho các tác vụ như Machine Translation. Kiến trúc này sử dụng một Encoder với Self-Attention và MLP nhằm đọc và hiểu được tốt Input ở ngôn ngữ A. Sau đó, Decoder với Causal Self-Attention và MLP có tác dụng Generate Output đã được dịch sang ngôn ngữ B ở dạng Token-by-Token hay Autoregression. Ngoài ra, Cross-Attention cũng được dùng để Decoder có thể trích xuất được thông tin từ Encoder. Causal Self-Attention sử dụng một Causal Mask để ngăn Decoder nhìn trước các Token trong tương lai và đảm bảo nó chỉ có thể học được từ các Token trong quá khứ.

- Encoder-only:

  - Là dạng Variant của Transformer phục vụ một số tác vụ khác đặt nặng việc trích xuất thông tin như Question Answering hay Sentence Classification. Một trong những ví dụ điển hình của kiến trúc này là Bidirectional Encoder Representations from Transformers (BERT). BERT hướng tới việc học được Bidirectional Context bằng cách sử dụng Masked Language Modeling (MLM) để Mask ngẫu nhiên 15% các Token rồi dự đoán chúng cùng với Next Sentence Prediction (NSP) nhằm dự đoán liệu Sentence B có nằm sau Sentence A hay không. Với Sentence Classification, BERT dùng một Classification Token đặc biệt gọi là [CLS] được đặt ở đầu mỗi Input Sequence nhằm tạo ra một [CLS] Output Token có khả năng tóm tắt toàn bộ câu và được Feed cho Classifier Layer cho việc phân loại chẳng hạn như trong Sentiment Analysis. Tuy nhiên, các Encoder-only Model như BERT không còn được sử dụng rộng rãi do thiếu khả năng Generate Text thực sự hiệu quả.

- Decoder-only:

  - Là dạng Variant của Transformer thực sự hiệu quả và đứng đằng sau các LLM như GPT. Không cần sử dụng Encoder vì chỉ cần hiểu và Generate được trên cùng một Sequence, Decoder-only cũng là một dạng Autoregressive Model sử dụng Causal Self-Attention và MLP. Ngoài ra, nó cũng dùng một [Extract] Token đặc biệt cho Classification tuy nhiên khác với Encoder-only, Token này phải được đặt ở cuối câu thì mới có thể Attend được các Token còn lại. Đây là một kiểu Architecture cực kỳ hiệu quả trong Training do sử dụng một Technique gọi là Teacher Forcing. Đầu tiên, Input Sequence cần được Shift sang phải 1 Token và sau đó trở thành Ground Truth để Model học cách Predict Token tiếp theo cho tất cả các Input Token một cách đồng thời. Nhờ đó, khác với các Sequence Models truyền thống hoạt động bằng cách Generate và Feed lại từng Output Token theo trình tự lần lượt với tốc độ học chậm và rủi ro Snowball / Compound Errors cao, Teacher Forcing cho phéo Model Train đúng và đồng thời Ground Truth ở mọi Step. Do vậy, Decoder-only chính là kiến trúc mạnh nhất cho việc Generate, Embed và thậm chí cả Memorize dữ liệu

- Sequence Models:
  - Là các dạng Model (RNNs, LSTM, GRU ...) vốn bị hạn chế rất lớn so với Transformer trong quá khứ. Tuy nhiên, các Sequence Models mới như Mamba đã giải quyết được đáng kể những hạn chế này. Thay vì Self-Attention, Mamba sử dụng một State Space Operator hoạt động tương tự như các Recurrent Cell trong RNN tuy nhiên lại hoàn toàn Differentiable và Parallelizable. Với mỗi Time Step, Mamba Update một Internal Hidden State là một Recurrence Relation $x_t = Ax_{t - 1} + Bu_t$ với $u_t$ là Input Embedding và Output $y_t = Cx_t$. Khác với RNN, Mamba có khả năng Unroll State Space của mình để cho phép Parallel Training và do đó tiệm cận tốc độ Train với Transformer. Thậm chí, tốc độ Inference của Mamba còn có phần nhỉnh hơn Transformer do Hidden State liên tục được Update $O(n)$ và có thể lưu trữ toàn bộ Context của Sequence thay vì phải thực hiện $O(n^2)$ Self-Attention và lưu trữ các Key / Value Pairs trong Memory. Tuy nhiên, điểm yếu của Mamba đó là Hidden State sẽ trở thành một Bottleneck nếu phải chứa tất cả Context của một Sequence quá dài trong một State Space có kích thước giới hạn. Nếu không thể thực hiện điều này, Mamba sẽ không thể vượt qua được Transformer về độ hiệu quả trong tương lai
