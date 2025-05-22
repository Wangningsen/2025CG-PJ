import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
w1=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.sketch().segment((-4,68),(72,68)).arc((34,100),(-4,68)).assemble().finalize().extrude(82).union(w1.sketch().arc((-72,-41),(-53,-65),(-23,-77)).segment((-23,-100)).segment((3,-100)).segment((3,-74)).arc((41,-35),(32,19)).arc((38,-11),(29,-40)).arc((20,-59),(3,-70)).segment((3,-47)).segment((-23,-47)).segment((-23,-70)).arc((-26,-69),(-30,-67)).arc((-54,-59),(-72,-41)).assemble().finalize().extrude(-4))