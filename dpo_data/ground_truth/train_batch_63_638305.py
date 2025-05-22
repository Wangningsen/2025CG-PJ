import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
r=w0.sketch().segment((8,-48),(73,-48)).arc((40,-26),(8,-48)).assemble().finalize().extrude(-95).union(w0.sketch().segment((-73,-13),(39,-13)).segment((39,48)).segment((32,48)).arc((-20,-10),(-72,48)).segment((-73,48)).close().assemble().finalize().extrude(105))