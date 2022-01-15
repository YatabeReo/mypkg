

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

rosnode list
 ```
 ```
 
rostopic list
 ```
 ```

rostopic echo /count_up
 ```



 # ライセンス

Copyright (c) 2021 Ryuich Ueda

Copyright (c) 2021 Reo Yatebe



> This program is free software; you can redistribute it and/or
> modify it under the terms of the GNU General Public License
> as published by the Free Software Foundation; either version 2
> of the License, or any later version.

> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
> GNU General Public License for more details.

> You should have received a copy of the GNU General Public License
> along with this program. If not, see http://www.gnu.org/licenses/.
