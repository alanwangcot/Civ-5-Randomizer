## 文明5联机随机文明生成 Civ 5 multiplayer random civ generator

基于PyQt6框架实现的GUI版文明5联机随机文明生成器，PvP前摇一摇！


### UPDATE
-   一键禁用/解禁功能已修好，可频繁多次点击，也不会再卡死程序了。

### FEATURES
-   支持选择2-10人，每人1-8个文明
-   禁用文明，一键禁用4个一级文明和9个二级文明，一二级文明和威尼斯默认禁用
-   检测`人数` 乘以 `每人文明数`确保总文明数够用
-   随机奇迹作为获胜条件，2-8名玩家随机三个奇迹，其中至多只有一个前期奇迹

### TODOS
-   Multi-language support, English localization
-   Fix assets used so UI isn't fked up at random places

### KNOWN BUGS
-   Algorithm to randomize wonders has a close to zero but non-zero chance to never return. Shouldn't be a big problem though. If unlucky enough kill the app and reroll.
-   Layouts are messed up in some places due to me not knowing how to properly align things with PyQt. Also am not a graphic designer so ugly GUI will do.

### LICENSE
-   As the PyQt6 library is used for this project, it is therefore published under the GPL license. See the LICENSE file.