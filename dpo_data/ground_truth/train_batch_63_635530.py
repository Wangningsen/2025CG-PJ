import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().segment((-17,-100),(-17,-44)).segment((54,-44)).arc((52,-37),(50,-29)).arc((68,-9),(69,18)).arc((63,97),(7,41)).arc((-9,23),(-11,-1)).arc((-49,-48),(-17,-100)).assemble().push([(29,6)]).circle(27,mode='s').finalize().extrude(-128).union(w0.workplane(offset=72/2).moveTo(-70,-54.5).box(42,29,72))