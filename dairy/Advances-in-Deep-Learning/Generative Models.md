# Discriminative Models

Trái ngược với Generative Models là các Discriminative Models có khả năng Extract được một thông tin gì đó từ Input X để liên hệ và chuyển hoá nó thành Output Y. Đây chính là các kiểu Model đã rất quen thuộc thường được sử dụng cho các tác vụ như Regression hay Classification. Chúng ta có thể mô phỏng các dạng Model này bằng Conditional Probability $P(Y|X)$ với $Y$ là Label và $X$ là dữ liệu. Thông thường, Output $Y$ luôn được định nghĩa rõ ràng và Distribution của $P(y|x)$ tương đối dễ xác định.

# Generative Models

Tuy nhiên, các Discriminative Models không có khả năng học được cách dữ liệu được sản sinh ra như thế nào. Ví dụ, thay vì chỉ học Label của Image, chúng ta muốn các Model có thể hiểu được cách tạo ra các Image mới. Đó là lý do các Generative Models được ra đời, và chúng ta có thể mô phỏng chúng bằng $P(X)$.

Với một Generative Model $P(X)$, chúng ta kì vọng chúng có thể học được Distribution của dữ liệu $X$ và từ đó thực thi được 2 tác vụ sau:

- **Sampling** để tạo ra được các Sample $x$ mới từ $P(X)$ hay $x \sim P(X)$

- **Density Estimation** để dự đoán được xác suất của một $x$ từ $P(X)$ hay $P(X = x)$

Tuy nhiên, cả 2 tác vụ trên đều tương đối là khó nhằn và đó là lý do Generative Modelling thường khó và nặng về lý thuyết hơn so với Discriminative Modelling.

- Với **Density Estimation**, cái khó đến đến từ việc làm sao để đảm bảo tổng Probability của tất cả các Input $x$ bằng 1 hay $\sum_{x}P(x) = 1$

- Trong khi đó, **Sampling** khó bởi chúng ta cần xác định xem nên sử dụng Input là gì để Train Model

# Variational Autoencoder (VAE)

Là một trong những Generative Model đầu tiên, Autoencoder tập trung vào việc học một Encoder $z = f_{E}(x)$ có khả năng Compress một High-Dimensional Input $x$ như Image về một Latent Vector $z$ ở Lower-Dimension. Đồng thời, một Decoder $\hat{x} = f\_{D}(z)$ cũng được dùng để Reconstruct $x$ ban đầu từ Latent Vector $z$. Sau đó, Model được Train bằng cách Minimize Reconstruction Loss $l = E_{x}[|f_{D}(f{E}(x)) - x|]$ đến từ sự khác biệt giữa Input ban đầu và Output sau khi đã Reconstruct. Nhờ vậy, sau khi Train trên thật nhiều Image chúng ta hi vọng Autoencoder có thể học được một Compressed Representation có ý nghĩa từ Input và có khả năng Generate các Sample mới, tương đồng.

Tuy nhiên, nếu chỉ đơn thuần ở dạng Vanilla, Autoencoder không thực sự hiệu quả trong việc Generate các Sample mới do bản chất Compression khó có thể thực sự biểu đạt được cấu trúc của Image. Để giải quyết được yếu điểm này, chúng ta có thể chuyển hoá các Encoder và Decoder thành dạng _Probabilistic_ và từ đó thêm phần _Variational_ vào Autoencoder.

VAE hoạt động bằng cách sử dụng Decoder $P_{D}(x | z)$ và Encoder $P_E(z | x)$ thay vì $f\_{D}(z)$ và $f_{E}(x)$. Có thể thấy, Decoder và Encoder giờ đây hoạt động rất giống với các Discriminative Models. Ngoài ra, VAE cũng cần dùng một Assumption rất lớn đó là Distribution của $Z$ là Normal hay $P(Z) = \mathcal{N}(0, 1)$. Điều này là cần thiết để biểu thị và học được được mối liên hệ giữa $P(x)$ và $P(z)$ thông qua phương trình:

$$P(x) = \sum_{z}P_{D}(x | z)P(z)$$

Nói cách khác, chúng ta có thể dễ dàng Generate một Image mới hay Sample một $x \sim P(X)$ bằng cách Sample một $z \sim P(Z)$ và một $x \sim P(x | z)$. Ngoài ra, chúng ta cũng có thể biểu thị mối quan hệ mật thiết giữa Probabilistic $P(Z)$, Decoder $P_{D}(x | z)$ và Encoder $P_E(z | x)$ bằng Bayes' Rule:

$$P_{E}(z | x) = \frac{P_{D}(x | z)P(z)}{P(x)}$$

Equation trên rất đẹp để liên hệ các thành phần với nhau tuy nhiên cũng khó có thể giải được do $P_{E}(z|x)$ là Intractable. Thay vì giải trực tiếp, chúng ta có thể Approximate một $Q \approx P_{E}$ bằng cách Minimize Kullback-Leibler (KL) Divergence giữa $Q$ và $P_{E}$:

$$D_{KL}(Q(z | x) || P_{E}(z | x)) = logP(x) + E_{z \sim Q}[log\frac{P(z)P_{D}(x|z)}{Q(z|x)}]$$

Cũng dễ thấy với Equation trên, nếu 2 Distribution càng giống nhau thì KL Divergence càng tiếp cận 0:

$$\frac{P(z)P_{D}(x|z)}{Q(z|x)} \to 1$$

$$log\frac{P(z)P_{D}(x|z)}{Q(z|x)} \to 0$$

$$D_{KL}(Q(z | x) \| P_{E}(z | x)) \to 0$$

Chúng ta có thể viết lại Equation này ở dạng sau đây:

$$logP(x) - D_{KL}(Q(z | x) || P_{E}(z | x)) = E_{z \sim Q}[log\frac{Q(z|x)}{P(z)P_{D}(x|z)}]$$

với $E_{z \sim Q}[log\frac{Q(z|x)}{P(z)P_{D}(x|z)}]$ chính là Negative của $E_{z \sim Q}[log\frac{P(z)P_{D}(x|z)}{Q(z|x)}]$.

Do đó, thay vì Minimize, chúng ta cần Maximise $logP(x) - D_{KL}(Q(z | x) || P_{E}(z | x))$ bằng 2 cách:

- Maximise $logP(x)$
- Minimise $D_{KL}(Q(z | x) || P_{E}(z | x))$

Phương pháp này còn được gọi là ELBO (Evidence Lower Bound) và có thể được biểu thị một cách khác bởi Equation sau:

$$-\frac{1}{2}\mathbb{E}_{z \sim Q}[\|x - \mu_D(z)\|_2^2] -\frac{1}{2}(N\sigma_Q(x)^2 + \|\mu_Q(x)\|_2^2 - 2Nlog\sigma_Q(x)) + Const$$

Nhìn chung, các $\mu_{D}, \mu_{Q}, \sigma_{Q}$ trong Equation này nhắm tới việc đảm bảo 2 điều gồm:

- Approximate Distribution Q của Encoder $P_{E}(z|x)$ có thể tạo Latent Vector $z$ với Mean 0 và Standard Deviation 1 nhằm thoả mãn Assumption $P(Z) = \mathcal{N}(0, 1)$
- Mean của Reconstructed $\hat{x}$ từ Latent Vector $z$ bởi Decoder giống với Image $x$ ban đầu

Tuy nhiên, $z \sim Q$ cùng đồng nghĩa với việc chúng ta phải Sample $z$ và Sampling vốn là Non-Differentiable. Để giải quyết vấn đề này, một Reparameterization Trick được sử dụng nhằm Parameterize Encoder $Q$ thành một Normal Distribution dưới dạng $Q(z|x) = \mathcal{N}(z;\mu_{Q}(x),\sigma_{Q}^2(x))$ và nhờ đó, chúng ta có thể viết lại Sampling Objective trên như sau:

$$\mathbb{E}_{z \sim Q}[\|x - \mu_D(z)\|_2^2] = \mathbb{E}_{\epsilon \sim \mathcal{N}(0, 1)}[\|\mu_Q(x) + \epsilon\sigma_Q(x)\|_2^2]$$

Với $\epsilon \sim \mathcal{N}(0, 1)$, bản chất chúng ta đang Sample một Variable $\epsilon$ hoàn toàn Independent với $Q$ và nhờ đó, lược bỏ được bước Sampling trong Gradient Computation. Ngoài ra, $z$ cũng được thay thế bởi $\mu_{Q}(x) + \epsilon\sigma_{Q}(x)$ và nhờ vậy, Objective giờ đây hoàn toàn là Diffientiable và cho phép Backpropagation có thể được thực hiện.

Với VAE và các bước xử lý ở trên, chúng ta cuối cùng cũng đã có thể học được $P(X)$ và Sampling Function $x \sim P$ với khả năng Generate ra các Image mới. Tuy nhiên, VAE vẫn sở hữu một số yếu điểm chẳng hạn như:

- Reconstruction Loss sử dụng Pixel-level $L2-norm$ loss $\|\|_2^2$ dẫn tới Output có thể dễ bị Blurry
- Approximate Encoder Q được giả định là tuân theo Gaussian Distribution dẫn tới Output là các Gaussian Sphere ở trong High-dimensional Spaces có thể rơi vào 2 khả năng:
  - Quá Overlap với nhau và tạo ra Blurry Output
  - Quá tách rời nhau dẫn tới việc Sample ra các Parameters mà Model chưa từng được Train bằng và do đó tạo ra Garbage Output

# Generative Adversarial Networks (GANs)

Tương tự như VAE, GANs là một Sampling-based Model sử dụng Loss Function để Maximise được $P(x)$. Để làm điều này, GANs sử dụng một Deep Network Generator $G$ có khả năng chuyển đổi Random Noise $z$ thành các Image $x$ sao cho $x$ chúng có cùng Distribution với Dataset $\mathscr{D}$ hết sức có thể. Chúng ta có thể biểu thị bằng các phương trình sau:

$$x = G(z); z \sim \mathcal{N}(0, 1)$$

$$x \sim \mathscr{D}$$

Sử dụng khái niệm Two-Player Game, GANs cố gắng Match hai Distribution bằng cách:

- Player 1: Generator $G$ tạo Image từ Noise
- Player 2: Discriminator $D$ dự đoán xem các Image là Real (đến từ Dataset $\mathscr{D}$) hay Fake (được Generate bởi $G$)

Như vậy, quá trình Training sẽ hoàn thành khi Generator đủ tốt để Discriminator không thể phân biệt được giữa Real và Fake Image nữa. Có thể biểu thị Objective trên bằng Equation sau:

$$min_{G}max_{D}E_{x \sim G}[logD(x)] + E_{x \sim \mathscr{D}}[log(1 - D(x))] = min_{G}max_{D}E_{z \sim \mathcal{N}}[logD(G(x))] + E_{x \sim \mathscr{D}}[log(1 - D(x))]$$

Về bản chất, Equation này có thể được hiểu bằng việc chúng ta muốn Maximise khả năng phân biệt giữa Real và Fake Image của Discriminator nhưng lại Minimise sự khác biệt giữa chúng với Generator. Objective Function của GANs cũng được coi là tương đồng với việc Minimize Jensen-Shannon Divergence giữa Generated và Real Distribution của dữ liệu.

Như vậy, GANs đã cung cấp cho chúng ta một Generative Model hữu hiệu nữa có khả năng Generate các Image mới hiệu quả. Dưới đây là phân tích một số điểm mạnh yếu của mô hình này:

- Ưu:
  - Dễ Sample Image mới
  - Tự động học Pixel-Distance mà không đòi hỏi Reconstruction Loss dẫn tới Output Image chất lượng cao và không bị Blurry
- Nhược:
  - Min-Max Objective khó có thể được Optimize trong quá trình Training và do đó đòi hỏi một số Trick để hiệu quả hơn trong thực hành

# Flow-based Models

Khác với VAE và GANs, Flow-based Models là một trong những kiểu Model có khả năng thực hiện cả Sampling lẫn Density Esimation nhờ vào một kiểu kiến trúc đặc biệt mà trong đó, Generator $G$ bị thay đổi và không cần sử dụng đến Discriminator $D$. Sau đây là những thay đổi mà Flow-based Models áp dụng.

Đầu tiên, chúng thay thế Deep Network Generator $G$ thành một Invertible Network với Assumption rằng $z \to x$ là Invertible và $G^{-1}$ tồn tại và dễ tính toán. Do đó, Definition của $G$ cũng cần tuân theo Constraint đó là cả Input và Output đều có cùng Dimension hay $G: \mathbb{R}^N \to \mathbb{R}^N$

Nhờ Assumption này cộng với $P(Z) = \mathcal{N}(0, 1)$, chúng ta có thể vừa tính toán $P(x)$ lại vừa Optimize được $logP(x)$ dễ dàng. $P(x)$ bây giờ có thể được biểu thị bởi Equation sau:

$$P(x) = P(z)|det(\frac{\partial{z}}{\partial{x}})| = P(G^{-1}(x))|det(\frac{\partial{G^{-1}(x)}}{\partial{x}})|$$

Đây là một Closed-form Definition của $P(x)$ và để cho phép định nghĩa này, Flow-based Models cần sử dụng các Invertible Layer vừa giúp hình thành một Invertible Network vừa giúp dễ dàng tính toán Determinant của Jacobian. Mỗi Invertible Layer này được thực hiện như sau:

- Chia Inputs ra thành 2 nhóm $x_{1}, x_{2}$
- Chia Outputs ra thành 2 nhóm $y_{1}, y_{2}$
- $y_{1} = x_{1}$
- $y_{2} = exp(s(x_{1})) \odot x_{2} + t(x_{1})$

Ở dạng này, Inverse của Layer sẽ dễ dàng được tính toán theo công thức:

- $x_{1} = y_{1}$
- $x_{2} = exp(-s(y_{1})) \odot y_{2} + t(y_{1})$

Từ đó, chúng ta có một kiểu Generative Model mới có Performance tốt mà lại rất Stable trong việc Training. Tuy vậy, yếu điểm dễ thấy đó là Flow-based Models chỉ cho phép sử dụng một kiểu kiến trúc gồm các Invertible Layers khá hạn hẹp.

# Auto-Regressive Generation

Là một dạng Density-Based Model, Auto-Regressive Generation nhắm tới việc trực tiếp tính toán $P(x)$ bằng cách tính Probability của lần lượt từng Pixel trong Image, dựa trên Formula:

$P(x) = P(x_1)P(x_2 | x_1)P(x_3|x_1, x_2)P(x_4|x_1, x_2, x_3)...$

với $x_i$ là từng Pixel. Nhờ đó, việc Estimate $P(x)$ là tương đối dễ dàng. Ngoài ra, để Sample $x$ chúng ta cũng chỉ cần Sample lần lượt từng Pixel:

$$x_1 \sim P(X_1); x_2 \sim P(X_2 | x_1)$$

Có thể thấy, các dạng Model này có tốc độ Inference tương đối chậm do chỉ có thể Generate từng Pixel một. Tuy nhiên, thời gian Training không bị ảnh hưởng bởi điều này do có thể Train đồng thời tất cả các Pixel thông qua một phương pháp gọi là Teacher Forcing.

Ngoài ra, với các Sequence rất dài, Auto-Regressive Generation cũng gặp khó khăn bởi 2 yếu tố:

- Với những Pixel đầu tiên, Model cần Generate Output chính xác nếu không muốn làm ảnh hưởng tới tất cả các Pixel còn lại phụ thuộc vào chúng

- Với những Pixel cuối cùng, Model cần Capture được rất nhiều Dependencies của các Pixel trước đó để Generate được Output phù hợp

Do đó, một trong những cách giải quyết là sử dụng Tokenization / Vector-Quantization để làm ngắn Sequence lại, tuy nhiên với Trade-Off đó là $x_i$ thường trở nên phức tạp hơn.

Ngoài ra, Auto-Regressive Generation cũng cho phép Compress dữ liệu hiệu quả bởi nguyên tắc:

- Dữ liệu càng dễ đoán thì càng chứa ít thông tin và càng cần ít Bits để Encode
- Dữ liệu càng khó đoán thì càng chứa nhiều thông tin và càng cần nhiều Bits để Encode

Nhờ vậy, kết hợp với Arithmetic Coding, Auto-Regressive Generation cho phép phát triển lên một phương thức gọi là Adaptive Arithmetic Encoding thường được sử dụng trong Lossless Data Compression.

# Vector Quantization

Auto-Regressive Generation tuy là một kiểu Generative Model rất hiệu quả tuy nhiên ở dạng Vanilla lại có những hạn chế lớn đến từ Pixel-by-Pixel Generation. Thay vào đó, Vector Quantization cung cấp một phương pháp cho phép nhóm các Pixel thành từng Patch và do đó, khiến tác vụ trở nên đơn giản hơn rất nhiều đến từ 2 lý do:

- Nhiệm vụ sản sinh ra Patch mới giờ đây phụ thuộc vào một nhóm Pixel thay vì từng cái riêng lẻ
- Độ dài của Sequence ngắn hơn nhiều và do đó, Context mà các Patch cuối cần chứa đựng cũng nhỏ đi đáng kể

Quá trình này còn mang một tên gọi khác là Tokenization. Mỗi Patch $p_{i}$ chứa nhiều Pixel sẽ được quy đổi thành một Token $t_i \in {1, ..., K}$. Từ một Pixel Image $x \in \mathbb{R}^{H \times W \times 3}$ sẽ sản sinh ra một Token Image $z \in {1...K}^{h \times w}$ có Dimension giảm thiểu đi đáng kể.Nhờ đó, Autoregressive Model $P(t) = P(t_1)P(t_2 | t_1)P(t_3|t_1, t_2)P(t_4|t_1, t_2, t_3)...$ có thể được Train hiệu quả hơn

Tuy nhiên, làm thế nào để chúng ta có thể quy đổi từ một Continuous Image (gồm các Pixel) thành một Discrete Image (gồm các Token) mà vẫn đảm bảo Operation này là Differentiable?

Câu trả lời nằm ở một phương thức có tên gọi là Vector Quantization-Variational Autoencoder (VQ-VAE). Ngoài việc vẫn sử dụng Decoder $P_{D}(x | z)$ và Encoder $Q(z | x)$ là các Probability Distribution, phần VQ trong VQ-VAE phụ trách việc Quantize $z$ bằng cách lựa chọn Embedding gần nhất với nó trong một Codebook ${e_1...e_K}$ theo Formula $q(z) = argmin_{e_k}\|z - e_k\|$. Tuy nhiên, làm thế nào để chúng ta có thể Backpropagate qua Vector Quantization $q$ hay xác định $\nabla q(z)$?

Về bản chất, Vector Quantization $q(z)$ là Non-Differentiable. Tuy nhiên, chúng ta có thể dùng 1 Trick gọi là Straight-Through Estimator mang giả định $\nabla q(z) = I (identity)$. Dù đây là 1 Ugly Hack tuy nhiên nó vẫn đang được sử dụng thành công trong thực tế. Nhờ thế, Gradient vẫn có thể chạy qua VQ và cho phép Backpropagation hoạt động với VQ-VAE.

Dẫu vậy, VQ-VAE vẫn chỉ là một dạng Variant của VAE cho nên chịu chung những hạn chế về chất lượng Output. Ngoài ra, Cookbook càng sử dụng nhiều Bits thì số lượng Entry càng lớn Exponentially dẫn tới tiêu tốn nhiều GPU Memory và Gradients càng ngày càng Sparse làm chậm Training hơn.

Để cải thiện chất lượng Output, VQ-GAN là một giải pháp khác thay thế VAE bằng GAN và nhờ đó, trở thành dạng Tokenizer mặc định ngày nay. Tuy nhiên, các vấn đề liên quan đến kích thước của Codebook vẫn hiện hữu. Vì thế, các phương thức Quantization khác chẳng hạn như Lookup-Free Quantization (LFQ) cũng đã được phát triển. LFQ chỉ sử dụng các hàm đơn giản như $q(z) = sign(z)$ với $sign(z_i) = 1_{[z_i > 0] - 1_[z_i < 0]}$ và do vậy có thể loại bỏ hoàn toàn Codebook và các vấn đề liên quan tới nó.

# Dall-E

Là một trong những LLM Model lớn và thành công đầu tiên, Dall-E tận dụng việc có thể quy đổi cả Image lẫn Text thành các Token Stream để xây dựng một mô hình được Train và có thể Generate cả 2 dạng dữ liệu này dựa trên Formula $P(t| \hat{t} ) = P(t_1| \hat{t} )P(t_2|t_1, \hat{t} )...P(t_L|t_1,...,t_{L-1}, \hat{t} )$. Sử dụng các Dataset có cả Image lẫn Caption, kiểu kiến trúc Autoregression với Sparse Transformer, Mixed-precision và Shared Multi-GPU Training, Dall-E nhanh chóng trở thành Start-of-the-art ở thời điểm mới ra mắt với khả năng Generate các Image từ Text với chất lượng chưa từng thấy.

Xét về các góc độ khác nhau, những yếu tố cho phép Dall-E thực sự "cất cánh" phần lớn xuất phát từ số lượng và chất lượng của Dataset cũng như Scale điện toán khổng lồ. Về bản chất, Dall-E là một Model khá đơn giản tuy nhiên vẫn có thể đạt được Performance đáng kinh ngạc nhờ những yếu tố trên. Đây là một trong những bài học mà các DL Researchers liên tục nhận được trong suốt 10-15 năm qua.

# Diffusion Models

Là một trong những Generative Model cạnh tranh mạnh mẽ được với Autoregression về Performance. Thay vì mô phỏng Image theo từng Patch-by-Patch, Diffusion mô phỏng đồng thời toàn bộ Image bằng cách bắt đầu với một phiên bản $x_0$ hoàn toàn sạch, sau đó dần dần thêm Noise $q(x_t | x_{t-1}) = \mathcal{N}(\sqrt{1 - \beta}x_t, B_tI)$ qua từng Step $t$ với $\beta_t$ tăng dần theo $t$. Điểm đặc biệt đó là do sử dụng Gaussian Noise, chúng ta có thể tính toán được $q(x_t|x_0)$ bằng một Closed-form Equation:

$$q(x_t|x_0) = \int\prod^t_{i=1}q(x_i|x_{i - 1})dx_{1...t-1} = \mathcal{N}(\sqrt{\bar{\alpha}_t}x_0, (1 - \bar{\alpha}_t)I)$$

với $\bar{\alpha}_t = \prod^t_{i=1}(1 - \beta_i)$. Vậy, mục đích của việc thêm Noise này là gì?

Từ một Noisy Image, Diffusion muốn học một quá trình ngược lại nhằm loại bỏ Noise để lấy được ảnh gốc. Nếu làm được điều này, về bản chất Diffusion sẽ có thể Generate các Image mới trực tiếp từ Noise. Chúng ta cũng có thể mô phỏng quá trình ngược lại này với $P(x_t) = \mathbb{N}(0, I)$ và Denoise Distribution $P(x_{t - 1} | x_t) = \mathbb(\mu_\theta(x_t), \sum_\theta(x_t))$ bằng Formula sau:

$$P(x_{0...T}) = P(x_T)\prod^T_{t=1}P(x_{t-1}|x_t)$$

$$P(x_0) = \int P(x_{0...T})dx_{1...T}$$

với $P(x_0)$ cho phép xác định được xác suất của Image $x_0$. Tuy nhiên, việc tính xác suất $P(x_0)$ là Intractable vì đòi hỏi Integrate qua tất cả các $x_{1...T}$ có thể được Generate. Thay vì thế, chúng ta có thể Maximise Evidence Lower Bound (ELBO):

$$logP(x_0) \ge E_q[log\frac{P(x_{0...T})}{q(x_{1...T}|x_0)}]$$

Tuy khá nặng lý thuyết toán, phần thuật toán của Diffusion lại tương đối đơn giản bao gồm 2 phần:

- Training: Chọn một Random Image, thêm Random Noise vào nó và sau đó dự đoán chúng ta đã thêm Noise gì

- Sampling: Chọn một Random Noise, dần dần Remove Noise từ nó để Generate được Image mới

Để Train được, Diffusion đòi hỏi một kiểu kiến trúc U-Net có khả năng Downsample Input và sau đó Upsample để tạo ra Output có cùng Dimension. Ngoài ra, kết nối giữa các Downsample và Upsample Layer là các Skip Connections. Tới năm 2021, Guided Diffusion được Publish với một số đặc điểm giúp nó thực sự trở thành State-of-the-art:

- Học Variance $\sum(x_t)$
- Architecture Scale lớn hơn với nhiều Layer, Attention Head, ... hơn
- Sử dụng Classifier Guidance (còn gọi là Conditioning) nhằm định hướng Model tới việc Generate các Image thuộc một số Label cụ thể. Từ đó, chúng ta có thêm khả năng kiểm soát quá trình Denoise để tạo ra các Image theo ý muốn hơn

Như vậy, nhìn chung Diffusion là một dạng Model có thể Generate các Output Image có chất lượng cao. Tuy nhiên, nó khá là khó kiểm soát và rất tốn kém về mặt điện toán với nhiều bước Sampling lẫn đòi hỏi cả Input và Output phải đều có độ phân giải cao

# Latent Diffusion

Nhằm giải quyết vấn đề lớn nhất của Diffusion đó là tốn kém về điện toán, Latent Diffusion sử dụng thêm Autoencoder nhằm Encode các Patch của Image thành một Latent Code ở Low Dimension, sau đó Decode lại thành High Dimension Output. Diffusion do đó sẽ được chạy trực tiếp trên các Latent Code sử dụng kiến trúc U-Net. Ngoài ra, Model cũng được Condition với các dữ liệu Text, Image, Semantic Map, ... Nhờ Autoencoder, tốc độ Training và Generation sẽ gia tăng đáng kể và chúng ta có thể áp dụng Diffusion lên cả những Image ở độ phân giải cao. Mô hình Imagegen của Google chính là một trong những Diffusion Model có Scale lớn đầu tiên như vậy. Tương tự, OpenAI cũng cho ra mắt Dall-E 2 / 3 với kiến trúc gần như tương tự.

Vậy một khi đã có một Model có khả năng Generate các Image bất kỳ từ Text Prompt rồi, thì chúng ta cần làm gì tiếp?

Tuy đã có khả năng tạo ra các Image rất chất lượng và rõ nét, sẽ là khá khó để có thể điều khiển các yếu tố như vị trí, cấu trúc hay Layout của các Output Image. Do vậy, hướng tập trung tiếp theo nhắm đến việc Control được các Output của Latent Diffusion này hơn không chỉ dừng lại ở việc Conditioning lên Text. Bắt đầu với một mô hình Latent Diffusion đã được Pre-trained, chúng ta muốn Condition bằng các Input khác chẳng hạn như từ các Sketch hay Pose Tracks để định hướng cấu trúc. Sử dụng một Copy của Encoder với các Input thêm vào và các Zero-initialised Convolution Layer với Weights 0, chúng ta sẽ có khả năng Generate được các Output Image tuân theo định hướng như mong muốn. ControlNet chính là một trong những kiểu kiến trúc này.

# Nên sử dụng Generative Model nào?

Với nhiều công cụ trong tay, làm sao để biết nên lựa chọn cái nào trong trường hợp nào. Sau đây sẽ là một số gợi ý để lựa chọn các Generative Model tương ứng với Use Case:

- Nếu một Pre-trained Model đã sẵn có:
  - Và bạn có nhiều tài nguyên Compute: Tự Train Diffusion hoặc Autoregressive của riêng mình
  - Nhưng bạn có ít tài nguyên Compute: Fine-tune các Diffusion hoặc Autoregressive sẵn có
- Nếu không có sẵn Pre-trained Model:
  - Và bạn có nhiều dữ liệu + Compute: Tự Train Diffusion hoặc Autoregressive của riêng mình
  - Nhưng bạn có ít dữ liệu + Compute: Tự Train Variational Autoencoder tuy nhiên Output sẽ Low Resolution
