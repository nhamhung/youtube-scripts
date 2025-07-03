# Discriminative Models

Trái ngược với Generative Models là các Discriminative Models có khả năng Extract được một thông tin gì đó từ Input X để liên hệ và chuyển hoá nó thành Output Y. Chúng thường được sử dụng cho các tác vụ như dự đoán hay phân loại. Chúng ta có thể mô phỏng các dạng Model này bằng Conditional Probability $P(Y|X)$ với Y là Label và $X$ là dữ liệu. Thông thường, Output Y luôn được định nghĩa rõ ràng và Distribution của $P(y|x)$ tương đối dễ xác định

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

$$D_{KL}(Q(z | x) || P_{E}(z | x)) \to 0$$

Chúng ta có thể viết lại Equation này ở dạng sau đây:

$$logP(x) - D_{KL}(Q(z | x) || P_{E}(z | x)) = E_{z \sim Q}[log\frac{Q(z|x)}{P(z)P_{D}(x|z)}]$$

với $E_{z \sim Q}[log\frac{Q(z|x)}{P(z)P_{D}(x|z)}]$ chính là Negative của $E_{z \sim Q}[log\frac{P(z)P_{D}(x|z)}{Q(z|x)}]$.

Do đó, thay vì Minimize, chúng ta cần Maximise $logP(x) - D_{KL}(Q(z | x) || P_{E}(z | x))$ bằng 2 cách:

- Maximise $logP(x)$
- Minimise $D_{KL}(Q(z | x) || P_{E}(z | x))$

Phương pháp này còn được gọi là ELBO (Evidence Lower Bound) và có thể được biểu thị một cách khác bởi Equation sau:

$$-\frac{1}{2}\mathbb{E}_{z \sim Q}[\|x - \mu_{D}(z)\|_2^2] -\frac{1}{2}(N\sigma_{Q}(x)^2 + \|\mu_{Q}(x)\|_2^2 - 2Nlog\sigma_{Q}(x)) + Const$$

Nhìn chung, các $\mu_{D}, \mu_{Q}, \sigma_{Q}$ trong Equation này nhắm tới việc đảm bảo 2 điều gồm:

- Approximate Distribution Q của Encoder $P_{E}(z|x)$ có thể tạo Latent Vector $z$ với Mean 0 và Standard Deviation 1 nhằm thoả mãn Assumption $P(Z) = \mathcal{N}(0, 1)$
- Mean của Reconstructed $\hat{x}$ từ Latent Vector $z$ bởi Decoder giống với Image $x$ ban đầu

Tuy nhiên, $z \sim Q$ cùng đồng nghĩa với việc chúng ta phải Sample $z$ và Sampling vốn là Non-Differentiable. Để giải quyết vấn đề này, một Reparameterization Trick được sử dụng nhằm Parameterize Encoder $Q$ thành một Normal Distribution dưới dạng $Q(z|x) = \mathcal{N}(z;\mu_{Q}(x),\sigma_{Q}^2(x))$ và nhờ đó, chúng ta có thể viết lại Sampling Objective trên như sau:

$$\mathbb{E}_{z \sim Q}[\|x - \mu_{D}(z)\|_2^2] = \mathbb{E}_{\epsilon \sim \mathcal{N}(0, 1)}[\|\mu_{Q}(x) + \epsilon\sigma_{Q}(x)\|_2^2]$$

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
