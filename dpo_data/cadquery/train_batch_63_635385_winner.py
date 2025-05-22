import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.workplane(offset=-64/2).moveTo(-56,20).cylinder(64,32).union(w0.sketch().segment((57,-49),(58,-52)).segment((68,-47)).arc((62,-48),(57,-49)).assemble().reset().face(w0.sketch().segment((78,-41),(88,-36)).segment((86,-33)).arc((82,-38),(78,-41)).assemble()).finalize().extrude(136))