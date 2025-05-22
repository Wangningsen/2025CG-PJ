import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().arc((-87,26),(-92,-10),(-57,-1)).arc((-26,63),(-87,26)).assemble().finalize().extrude(-81).union(w0.sketch().push([(49,-22)]).circle(51).push([(37,-22)]).rect(6,16,mode='s').finalize().extrude(6))