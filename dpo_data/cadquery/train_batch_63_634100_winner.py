import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('XY',origin=(0,0,-2))
r=w0.sketch().arc((11,58),(-60,11),(20,-12)).arc((22,-11),(23,-8)).arc((24,-11),(24,-15)).segment((100,-15)).segment((100,84)).segment((24,84)).segment((24,69)).arc((17,64),(11,58)).assemble().push([(38,45)]).circle(28,mode='s').push([(-29,-58)]).circle(26).finalize().extrude(77).union(w1.workplane(offset=-41/2).moveTo(-75.5,-65).box(5,70,41))