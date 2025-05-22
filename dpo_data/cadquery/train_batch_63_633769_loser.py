import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-42,-78),(25,-78)).segment((25,-47)).segment((37,-60)).segment((45,-44)).arc((99,-4),(31,6)).arc((13,17),(-6,8)).segment((-30,8)).arc((-79,72),(-42,1)).close().assemble().finalize().extrude(12)