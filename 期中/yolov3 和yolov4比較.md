# yolov3 和yolov4比較
## YOLOv4 介紹
YOLO最早於2015年6月由Joseph Redmon提出，而YOLO所擁有的物件偵測技術使其在電腦視覺領域有一定的地位，而後來跟著時間的推進，YOLO的版本也逐漸更新，如YOLOv2、YOLOv3。而本專題採用的YOLOv4則是由俄羅斯Alexey Bochkovskiy和台灣中央研究資訊院所的院長和博士共同開發，並且於AI Rewind 2020: A Year of Amazing Papers 榮獲 2020 年度最優秀的論文之一。而YOLOv4和前一代YOLO3的不同我們將在下面簡單進行介紹。
|	 | YOLOv3	| YOLOv4	| 為什麼要這樣改進 |
|--|--------|---------|-----------------|
| Backbone	  | Darknet53	| CSPDarknet53	| 參數量減少，進而減少運算量，甚至能提高準確率
| Neck	| FPN|	PANet + SPP	| 提升局部特徵和全局特徵的融合，進而豐富最終特徵圖的表達能力
## backbone由Darknet53改為CSP Darknet53
影像辨識通常用於小型的裝置上，因此需要降低模型所需的計算量，以減短辨識預測時間，CSP Darknet53 為以Darknet為基礎結合CSPNet所產生，

CSPNet的作者為了降低網路優化中的梯度訊息重複度，作者透過將Base layer 的 feature map 劃分為2個部分，然後再經過transition -> concatenation -> transition 將2個部分融合起來，


這樣的作法使得CSPNet儘管將模型進行了輕量化處理，但在提升CNN學習力的同時仍然能夠保持準確性，同時CSPNet也達成了降低內存占用和降低計算的作用。

![]( https://github.com/kaifeng273/ai111b/blob/main/%E6%9C%9F%E4%B8%AD/3.png )
	 

 
## Neck 增加PANet和SPP 
SPP ( Spatial Pyramid Pooling 空間金字塔池化結構 ) 能夠根據不同的刻度大小對圖片進行劃分，捕捉到不同尺度下的細節信息。


同時，SPP 架構還具有固定大小的輸出，方便後續的分類和檢測任務。

![](https://github.com/kaifeng273/ai111b/blob/main/%E6%9C%9F%E4%B8%AD/1.png)

PANet 是以FPN 為基礎將原本相加的部分修改為合併，以犧牲計算量達到效果提升
![]( https://github.com/kaifeng273/ai111b/blob/main/%E6%9C%9F%E4%B8%AD/2.png ) 

