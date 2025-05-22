import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
w1=cq.Workplane('YZ',origin=(-10,0,0))
r=w0.sketch().arc((-17,69),(-37,-30),(64,-40)).segment((100,-40)).segment((100,84)).segment((98,84)).segment((98,93)).segment((64,93)).segment((64,80)).segment((82,80)).arc((37,36),(-17,69)).assemble().push([(-19,86.5)]).rect(34,13).finalize().extrude(-84).union(w1.sketch().arc((-93,-9),(-90,-9),(-92,-11)).arc((-79,-3),(-93,-9)).assemble().push([(-86,-7)]).circle(4,mode='s').finalize().extrude(-90))