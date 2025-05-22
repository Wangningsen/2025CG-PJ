import cadquery as cq
w0=cq.Workplane('YZ',origin=(59,0,0))
r=w0.sketch().segment((-100,3),(-24,3)).segment((-24,26)).segment((-100,65)).close().assemble().push([(-6,-55)]).circle(10).finalize().extrude(-118).union(w0.sketch().arc((99,-20),(100,-13),(99,-5)).close().assemble().finalize().extrude(-55))