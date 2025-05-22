import cadquery as cq
w0=cq.Workplane('YZ',origin=(74,0,0))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.sketch().arc((-32,-62),(-18,-64),(-17,-72)).arc((28,-63),(36,-16)).segment((15,-16)).segment((15,-14)).segment((35,-14)).arc((-25,-1),(-32,-62)).assemble().finalize().extrude(-157).union(w0.sketch().segment((-66,-20),(-42,-20)).segment((-42,-40)).segment((-43,-40)).arc((-41,-42),(-39,-45)).arc((-14,-71),(-22,-97)).arc((55,1),(-66,-20)).assemble().finalize().extrude(-30)).union(w1.workplane(offset=94/2).moveTo(58,-0.5).box(50,5,94))