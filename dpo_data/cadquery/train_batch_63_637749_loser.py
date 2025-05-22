import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-72))
r=w0.sketch().arc((86,-22),(92,-26),(100,-27)).arc((93,-24),(86,-22)).assemble().finalize().extrude(14).union(w0.sketch().arc((-74,41),(-47,-52),(-21,40)).arc((-47,98),(-74,41)).assemble().push([(-70,-22)]).circle(20,mode='s').push([(-8,-80)]).circle(18).finalize().extrude(144))