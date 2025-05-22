import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().segment((28,48),(38,47)).segment((39,51)).segment((29,52)).close().assemble().reset().face(w0.sketch().segment((92,63),(97,62)).segment((100,65)).segment((93,68)).close().assemble()).finalize().extrude(-12).union(w0.sketch().arc((-100,-22),(-86,-56),(-52,-66)).arc((-32,-65),(-23,-47)).arc((-27,1),(-75,16)).arc((-80,-12),(-100,-22)).assemble().finalize().extrude(79)).union(w1.sketch().push([(25.5,-14)]).rect(65,106).push([(26,-14)]).circle(2,mode='s').finalize().extrude(-100))