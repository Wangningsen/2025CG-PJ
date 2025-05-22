import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
w1=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.workplane(offset=-30/2).moveTo(17.5,58.5).box(49,57,30).union(w0.sketch().push([(-91,-3)]).circle(9).push([(75,-17)]).circle(25).push([(67,-24)]).circle(6,mode='s').push([(87,-12)]).circle(3,mode='s').finalize().extrude(-26)).union(w1.sketch().segment((-87,-46),(10,-46)).segment((10,-16)).arc((27,33),(-25,33)).arc((-23,31),(-25,30)).arc((-27,25),(-28,20)).segment((-87,20)).close().assemble().push([(-50,-7.5)]).rect(8,5,mode='s').push([(1,13.5)]).rect(36,29,mode='s').finalize().extrude(69))