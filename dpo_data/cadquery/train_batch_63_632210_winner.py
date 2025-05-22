import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().arc((-88,26),(-94,-9),(-59,-1)).arc((-26,63),(-88,26)).assemble().finalize().extrude(-82).union(w0.sketch().push([(49,-22)]).circle(51).push([(35.5,-18.5)]).rect(5,9,mode='s').push([(70,-18.5)]).rect(5,9,mode='s').finalize().extrude(5))