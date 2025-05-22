import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-63))
w1=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.sketch().segment((-31,-100),(72,-100)).segment((22,-91)).segment((41,11)).segment((-31,11)).close().assemble().finalize().extrude(115).union(w1.sketch().push([(87,50)]).circle(13).reset().face(w1.sketch().segment((82,42),(91,42)).segment((91,44)).arc((93,50),(91,55)).segment((91,57)).segment((82,57)).segment((82,55)).arc((80,50),(82,44)).close().assemble(),mode='s').finalize().extrude(-60))