# Labyrinth Algorithms
 Different ways to generate and solve mazes in python
 
## Base Classes (Simple Yet Effective)
<p>Everything started with a single 'Cell'</p>
<img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/uml/Cell.png"
     alt="Everything started with a single 'Cell'"
     width="290"
     height="220"
     title="Everything started with a single 'Cell'">

<p>Then they formed 'Maze's to fulfill their destiny...</p>
<img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/uml/Maze.png"
     alt="Then they formed 'Maze's to fulfill their destiny"
     width="400"
     height="170"
     title="Then they formed 'Maze's to fulfill their destiny...">

## Algorithm Performances
<table>
<thead>
  <tr>
    <th rowspan="2"><br>Algorithm 🧙‍♂️<br></th>
    <th colspan="4">Labyrinth Size 📐<br>(ColxRow)</th>
    <th colspan="4">Generation Time 🕒<br>(seconds)</th>
  </tr>
  <tr>
    <td>50x50</td>
    <td>250x250</td>
    <td>1000x1000</td>
    <td>50x50</td>
    <td>250x250</td>
    <td>1000x1000</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>RecursiveBacktrackerAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>EllersAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>KruskalsAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>PrimsAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>RecursiveDivisionAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>AldousBroderAlgorithm</td>
    <td>✅</td>
    <td>✅</td>
    <td>❌</td>
    <td>0.3346393</td>
    <td>18.0111595</td>
    <td>❌</td>
  </tr>
  <tr>
    <td>WilsonsAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>HuntAndKillAlgorithm</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>GrowingTreeAlgorithm 🥉</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>0.0260674</td>
    <td>0.7234786</td>
    <td>12.2466479</td>
  </tr>
  <tr>
    <td>BinaryTreeAlgorithm 🥇</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>0.0176425</td>
    <td>0.4688853</td>
    <td>8.8348344</td>
  </tr>
  <tr>
    <td>SidewinderAlgorithm 🥈</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>0.0224984</td>
    <td>0.5559809</td>
    <td>10.595000</td>
  </tr>
</tbody>
</table>

## Some Results
<table>
<thead>
  <tr>
    <th rowspan="2">Algorithm 🧙‍</th>
    <th colspan="2">Labyrinth Size 📐</th>
  </tr>
  <tr>
    <td>50x50</td>
    <td>250x250</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>AldousBroder</td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/AldousBroder_50_50.PNG" width="150" height="150"></td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/AldousBroder_250_250.PNG" width="150" height="150"></td>
  </tr>
  <tr>
    <td>BinaryTree</td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/BinaryTree_50_50.PNG" width="150" height="150"></td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/BinaryTree_250_250.PNG" width="150" height="150"></td>
  </tr>
  <tr>
    <td>GrowingTree</td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/GrowingTree_50_50.PNG" width="150" height="150"></td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/GrowingTree_250_250.PNG" width="150" height="150"></td>
  </tr>
  <tr>
    <td>Sidewinder</td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/Sidewinder_50_50.PNG" width="150" height="150"></td>
    <td><img src="https://raw.githubusercontent.com/gokdumano/LabyrinthAlgorithms/main/images/results/Sidewinder_250_250.PNG" width="150" height="150"></td>
  </tr>
</tbody>
</table>

## Lots of Fun and Knowledge This Book Has 👽
<a href="http://www.mazesforprogrammers.com">
<img src="http://www.mazesforprogrammers.com/images/cover.jpg"
     alt="Lots of Fun and Knowledge This Book Has"
     width="300"
     height="380"
     title="Lots of Fun and Knowledge This Book Has...">
</a>
