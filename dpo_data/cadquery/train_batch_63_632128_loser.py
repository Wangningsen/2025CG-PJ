import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().arc((42,-81),(90,-84),(61,-47)).arc((-25,-20),(42,-81)).assemble().finalize().extrude(-73).union(w0.workplane(offset=-48/2).moveTo(17,23.5).box(60,105,48)).union(w0.sketch().push([(-8,15)]).circle(85).circle(11,mode='s').finalize().extrude(49))