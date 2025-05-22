import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
w1=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.sketch().arc((40,-82),(89,-86),(61,-47)).arc((-25,-20),(40,-82)).assemble().finalize().extrude(-73).union(w0.sketch().push([(-8,15)]).circle(85).circle(12,mode='s').finalize().extrude(49)).union(w1.sketch().segment((-72,-36),(-22,-36)).segment((-22,-50)).segment((13,-50)).segment((13,-36)).segment((76,-36)).segment((76,29)).segment((-72,29)).close().assemble().finalize().extrude(61))