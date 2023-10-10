'''
在Unity游戏中，提交到D3D11的TANGENT值并不是模型真实的TANGENT值，而是经过计算处理的值
在不清楚一款游戏具体使用何种方式计算TANGENT值时，在这里尽可能提供所有的TANGENT值的计算方法

注意计算TANGENT值需要 POSITION、NORMAL、TEXCOORD 三个输入

目前GIMI为了节省计算时间，选择了一种近似的算法而不是计算出原始的TANGENT
所以要么将Tailor改造成C++，要么TANGENT计算算法改写为C++
目前顶点数量超过20万就已经严重降低了运算速度，所以Tailor改写为C++似乎是很有必要的。


[TANGENT]
tangent_algorithm = Unity Standard Shader
tangent_algorithm = MikkTSpace
tangent_algorithm = Fitting Tangents
tangent_algorithm = Smooth Tangents
tangent_algorithm = Area Weighted Tangents
tangent_algorithm = Bitangent Reparameterization
tangent_algorithm = Dual Quaternions
tangent_algorithm = Implicit Representation


'''