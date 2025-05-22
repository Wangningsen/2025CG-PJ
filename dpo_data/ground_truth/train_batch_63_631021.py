import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
w1=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().arc((-85,34),(-48,-50),(-22,38)).arc((-54,50),(-85,34)).assemble().finalize().extrude(-79).union(w1.sketch().segment((-70,55),(21,55)).segment((21,59)).segment((38,59)).segment((38,55)).segment((70,55)).segment((70,100)).segment((-70,100)).close().assemble().push([(-52,82)]).circle(16,mode='s').push([(0,77.5)]).rect(18,41,mode='s').finalize().extrude(29))