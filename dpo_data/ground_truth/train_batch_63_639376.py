import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.sketch().segment((-50,-81),(-25,-100)).segment((50,-2)).segment((25,18)).close().assemble().push([(0,-41)]).circle(8,mode='s').push([(-15,67)]).circle(33).finalize().extrude(88)