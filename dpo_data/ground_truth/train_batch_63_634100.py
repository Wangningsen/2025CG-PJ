import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().arc((13,57),(-60,11),(24,-8)).segment((24,-15)).segment((100,-15)).segment((100,84)).segment((24,84)).segment((24,69)).arc((59,26),(13,57)).assemble().push([(-29,-58)]).circle(26).finalize().extrude(77).union(w1.workplane(offset=41/2).moveTo(-75.5,-65).box(5,70,41))