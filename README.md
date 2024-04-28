# modern_ai_for_beginners

> 我一直想在我的所有的B站系列视频想传递的一个概念是，既要懂代码实现，也要懂数学计算原理，或者反过来，不仅要懂原理，也要会实现；
> 原理与实践二者互为表里，不可分割。再者来说，实现是相对简单的，原理则是困难的，但是不懂原理，很难讲说深入了，就像不看源码，很难说自己懂这个框架了。
> 
> 这里补充介绍下我相关B站视频系列的一个很大的优势就是**数学**、**AI计算理论**以及**代码**的三位一体（当然受限于我自己的能力），可能没那么高的高度，但我追求的一种直观和实用，易理解，肯定是有的，是别的那里可能不是那么具备的。

modern AI for beginners

- 目前暂定的路线主要有如下两个分支，这两个分支统一来说都属于 Generative AI（生成式AI，也是某种形式的大一统），这是我对现代式 ai 的最直白最浅显的理解，然后在 multi modality 处汇合；
    - transformer based LLMs
    - diffusion models
    - multi modality
- 似乎目前越来越强的一个趋势，现代式人工智能越来越演变为一种复杂的大数据、深度学习为核心的复杂计算机科学系统工程的艺术；
    - 对一个人全面性的要求越来越高，但要分清主线和支线，支线仅是工具辅助支撑而已； 

## PyTorch、深度学习基础、数学基础

- 技术栈上主要是围绕 PyTorch 展开，如下我的 B 站系列（可能是最早稳定的一个）
    - [经典神经网络模型拓扑结构（pytorch）](htt就是数学、计算理论以及代码的三位一体（当然受限于我自己的能力），可能没那么高的高度，但我追求的一种直观，容易理解，肯定是有的；ps://space.bilibili.com/59807853/channel/collectiondetail?sid=446911)

- 数学基础，如下我的 B 站系列
    - [深度学习的数学基础](https://space.bilibili.com/59807853/channel/collectiondetail?sid=462509)
    - 目前我对数学基础的理解，
        - 矩阵分析；比较直观简单，拿来即用；
            - 矩阵矢量乘法，矩阵求逆；
            - 矩阵分解：奇异值分解（SVD）；
        - 数值优化方法；（这两块（优化和矩阵）的工具都比较成熟，大体了解下 solver 即可）
            - 对应torch 中的 optimizer，主要是基于数值优化的 gradient-based 的方法
        - 主要是概率与数理统计，贝叶斯（我觉得这部分的内容对我来说反而是困难的，因为比较抽象，需要较多的推导，）
            - 先验（prior），似然（likelihood），后验（posterior）；

- 深度学习
    - [Dive into Deep Learning](https://d2l.ai/)
        - 如果没有路径依赖果断选择 pytorch 版；

## Transformers based LLMs

主要是我在 B 站的三个系列

- [BERT、T5、GPT](https://space.bilibili.com/59807853/channel/collectiondetail?sid=496538)
    - 语言模型的基础
    - 一个练习项目：[Neural Network: Zero to hearo](https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&ab_channel=AndrejKarpathy) - Andrej Karpathy 制作的系列视频, 带你从 0 开始构造自己的 nanoGPT
- [personal chatgpt](https://space.bilibili.com/59807853/channel/collectiondetail?sid=1373266)
    - 大语言模型的全新范式
- [pytorch distributed](https://space.bilibili.com/59807853/channel/collectiondetail?sid=1384251)
    - 多级多卡分布式的基础
  
## diffusion models


## 软件工程与全栈

> 软件工程是复杂性管理的艺术；
> 但显然对于现代式人工智能而言，软件工程是工具是手段，而非目标；

- 我的 B 站系列
    - [全栈算法工程师](https://space.bilibili.com/59807853/channel/collectiondetail?sid=621084)
    - [软硬件知识](https://space.bilibili.com/59807853/channel/collectiondetail?sid=1280159)
- 代码好味道坏味道：[重构（第2版）](https://douban.com/book/subject/30468597/)

 
## tutorials based resources

- [Natural Language Processing with Transformers](./pdfs/Natural_Language_Processing_with_Transformers-2022-en.pdf)
- 强化学习篇
    - [openai 强化学习概念拾遗](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
    - [王树森 DRL](https://github.com/wangshusen/DRL)

- [Practical Deep Learning for Coders](https://course.fast.ai/) - Jeremy Howard (Kaggel 创始人) 制作的系列课程, 用自顶向下的方式, 从使用预训练模型开始深入到原理, 适合有软件开发经验的人入门
