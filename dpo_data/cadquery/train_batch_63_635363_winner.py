import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().segment((-29,-50),(-15,-55)).arc((-6,-65),(8,-64)).segment((23,-69)).segment((29,-54)).segment((15,-49)).arc((6,-39),(-8,-40)).segment((-23,-35)).close().assemble().finalize().extrude(94).union(w1.sketch().segment((-23,-14),(10,-14)).arc((0,-72),(59,-98)).segment((61,-98)).segment((68,-14)).segment((69,-14)).segment((69,36)).segment((-23,36)).close().assemble().finalize().extrude(36))