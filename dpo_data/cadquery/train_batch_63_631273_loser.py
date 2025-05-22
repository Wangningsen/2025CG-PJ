import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().segment((-100,-57),(23,-57)).arc((67,-68),(45,-32)).segment((45,-35)).segment((43,-35)).segment((43,-33)).arc((32,-38),(26,-49)).segment((26,-11)).segment((-100,-11)).close().assemble().push([(46,7.5)]).rect(2,77).push([(89.5,58.5)]).rect(21,41).finalize().extrude(-91)