import cadquery as cq
w0=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().segment((-100,7),(-97,4)).segment((-39,4)).segment((-39,-51)).segment((-12,-26)).segment((-24,-15)).arc((-36,16),(-68,22)).segment((-78,32)).close().assemble().finalize().extrude(-87).union(w0.sketch().segment((37,38),(85,19)).segment((85,-12)).segment((100,2)).segment((51,51)).close().assemble().finalize().extrude(20))