# mypkg
ロボットシステム学課題２のROSのリポジトリ

一秒間に五回二ずつ増えるcount.py

couny.pyの値を二倍にするtwice.pyがあります。

# 開発環境:
●OS系統

Ubuntu20.04

Raspberry Pi 4</span>

LANケーブル



# 基本的な動作：
### ラズパイを用いたカウントアッププログラム。

 ```
roscore
 ```
 ```
 chmod +x count.py
 ```
 ```
 source ~/.bashrc
 ```
 ```
 rosrun mypkg count.py
 ```
 ```
 rosrun mypkg twice.py
 ```
 ```
 rosnode list
 ```
 ```
 rostopic list
 ```
 ```
 rostopic echo /count_up
 ```
 ```
 rostopic echo /twice
 ```



 # ライセンス

Copyright (c) 2021 Ryuich Ueda

Copyright (c) 2021 Reo Yatebe

ライセンスは別ファイルLICENSEに記述してあるので読んでから使用してください。
