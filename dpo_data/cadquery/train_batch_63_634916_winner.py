import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((45,-34),(54,0),(45,34)).close().assemble().finalize().extrude(-200).union(w0.workplane(offset=-171/2).moveTo(-9,0).cylinder(171,45))