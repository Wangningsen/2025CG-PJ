import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().arc((12,-99),(15,1),(96,41)).arc((-81,52),(12,-99)).assemble().finalize().extrude(20).union(w1.workplane(offset=-19/2).moveTo(-6,-1).cylinder(19,12))