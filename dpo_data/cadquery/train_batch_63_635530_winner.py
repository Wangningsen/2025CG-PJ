import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().segment((-17,-100),(-17,-44)).segment((54,-44)).arc((53,-38),(50,-32)).arc((68,-8),(69,20)).arc((60,98),(8,40)).arc((-10,22),(-12,-2)).arc((-49,-44),(-17,-100)).assemble().push([(29,6)]).circle(27,mode='s').finalize().extrude(-128).union(w0.workplane(offset=72/2).moveTo(-70,-54.5).box(42,29,72))