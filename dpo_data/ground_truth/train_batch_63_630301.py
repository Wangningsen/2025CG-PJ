import cadquery as cq
w0=cq.Workplane('YZ',origin=(59,0,0))
r=w0.sketch().push([(-1,0)]).rect(134,158).reset().face(w0.sketch().arc((-64,57),(-32,33),(-48,69)).arc((-63,72),(-64,57)).assemble(),mode='s').finalize().extrude(-159).union(w0.sketch().arc((26,-22),(29,-39),(29,-56)).segment((38,-64)).segment((68,-30)).segment((35,-2)).arc((31,-12),(26,-22)).assemble().finalize().extrude(41))