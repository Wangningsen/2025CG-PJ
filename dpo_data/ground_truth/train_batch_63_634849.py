import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().arc((-5,92),(2,65),(-2,38)).arc((-98,-40),(18,-84)).arc((-9,-8),(68,-29)).arc((96,8),(95,54)).segment((95,53)).segment((85,56)).segment((88,68)).arc((46,98),(-5,92)).assemble().finalize().extrude(-100)