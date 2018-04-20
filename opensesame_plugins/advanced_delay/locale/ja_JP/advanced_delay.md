# Advanced_delay: ランダム遅延

`advanced_delay (ランダム遅延)` プラグインを用いることで指定した時間にランダムなマージンを追加し遅延を行うことができます。

- *Duration (遅延時間)* はms単位の遅延の平均時間を指します。
- *Jitter (ジッター)* はms秒単位の遅延の変動の大きさを表します。
- *Jitter mode (ジッターモード)* ではどのようにランダムなマージンを計算するか決めることができます:
	- *Standard deviation (標準偏差)* マージンを標準偏差とするガウス分布からの変動を計算。
	- *Uniform (一様分布)* 一様分布からマージンの変動を計算。