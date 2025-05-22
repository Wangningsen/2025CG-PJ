import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,76,0))
r=w0.sketch().segment((-89,-30),(18,-30)).arc((68,-95),(39,-18)).segment((39,10)).arc((-25,-23),(-89,10)).close().assemble().finalize().extrude(-173).union(w0.workplane(offset=-153/2).moveTo(-25,57).cylinder(153,14)).union(w0.sketch().arc((-88,27),(12,-2),(30,100)).arc((-18,46),(-88,27)).assemble().finalize().extrude(21))