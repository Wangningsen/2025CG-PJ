import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
w1=cq.Workplane('YZ',origin=(75,0,0))
r=w0.sketch().rect(46,200).push([(5,91)]).circle(7,mode='s').finalize().extrude(-151).union(w1.sketch().segment((-23,-14),(-17,-14)).arc((0,-20),(17,-14)).segment((23,-14)).segment((23,73)).segment((17,73)).arc((0,79),(-17,73)).segment((-23,73)).close().assemble().finalize().extrude(-133))