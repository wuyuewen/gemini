# Xen REST API

## VM

#### List

```GET /libvirt/xen/nodes/json```

Provide an description of all domains. The description may be reused
later to relaunch the domain with Create request.

Query Parameters:

- all - 1/True/true or 0/False/false, Show all domains except dom0.
Only running domains are shown by default (i.e., this defaults to false)
- flag - 0/1/2/4/8. Default ```0```.

```
0 - VIR_DOMAIN_XML_DEFAULT
1 - VIR_DOMAIN_XML_SECURE
2 - VIR_DOMAIN_XML_INACTIVE
4 - VIR_DOMAIN_XML_UPDATE_CPU
8 - VIR_DOMAIN_XML_MIGRATABLE
```

**Status Codes:**

- 200 - no error
- 400 - bad request
- 500 - server error

**Example request:**

```
GET /libvirt/xen/nodes/json HTTP/1.1
```

**Example response:**

```
HTTP/1.1 200 OK  
Content-Type: application/json  

[
    {
        "domain": {
            "@type": "xen",
            "clock": {
                "@offset": "utc"
            },
            "currentMemory": {
                "#text": "1048576",
                "@unit": "KiB"
            },
            "devices": {
                "console": {
                    "@type": "pty",
                    "target": {
                        "@port": "0",
                        "@type": "serial"
                    }
                },
                "controller": [
                    {
                        "@index": "0",
                        "@model": "ich9-ehci1",
                        "@type": "usb"
                    },
                    {
                        "@index": "0",
                        "@model": "ich9-ehci1",
                        "@type": "usb",
                        "master": {
                            "@startport": "0"
                        }
                    }
                ],
                "disk": [
                    {
                        "@device": "disk",
                        "@type": "file",
                        "address": {
                            "@bus": "1",
                            "@controller": "0",
                            "@target": "0",
                            "@type": "drive",
                            "@unit": "0"
                        },
                        "source": {
                            "@file": "/home/gemini/images/test0.raw"
                        },
                        "target": {
                            "@bus": "virtio",
                            "@dev": "hda"
                        }
                    },
                    {
                        "@device": "cdrom",
                        "@type": "file",
                        "address": {
                            "@bus": "1",
                            "@controller": "0",
                            "@target": "0",
                            "@type": "drive",
                            "@unit": "0"
                        },
                        "readonly": null,
                        "source": {
                            "@file": "/home/gemini/iso/CentOS-6.7-x86_64-minimal.iso"
                        },
                        "target": {
                            "@bus": "virtio",
                            "@dev": "hdc"
                        }
                    }
                ],
                "emulator": "/usr/lib64/xen/bin/qemu-system-i386",
                "graphics": {
                    "@autoport": "yes",
                    "@listen": "0.0.0.0",
                    "@port": "-1",
                    "@type": "vnc",
                    "listen": {
                        "@address": "0.0.0.0",
                        "@type": "address"
                    }
                },
                "input": [
                    {
                        "@bus": "usb",
                        "@type": "tablet"
                    },
                    {
                        "@bus": "ps2",
                        "@type": "mouse"
                    },
                    {
                        "@bus": "ps2",
                        "@type": "keyboard"
                    }
                ],
                "interface": {
                    "@type": "bridge",
                    "mac": {
                        "@address": "00:16:3e:4d:87:7d"
                    },
                    "source": {
                        "@bridge": "ovs0"
                    }
                },
                "serial": {
                    "@type": "pty",
                    "target": {
                        "@port": "0"
                    }
                },
                "video": {
                    "model": {
                        "@heads": "1",
                        "@type": "vga",
                        "@vram": "32768"
                    }
                }
            },
            "features": {
                "acpi": null,
                "apic": null,
                "pae": null
            },
            "memory": {
                "#text": "1048576",
                "@unit": "KiB"
            },
            "name": "test0",
            "on_crash": "restart",
            "on_poweroff": "destroy",
            "on_reboot": "restart",
            "os": {
                "boot": [
                    {
                        "@dev": "hd"
                    },
                    {
                        "@dev": "cdrom"
                    }
                ],
                "loader": {
                    "#text": "/usr/lib/xen/boot/hvmloader",
                    "@type": "rom"
                },
                "type": {
                    "#text": "hvm",
                    "@arch": "x86_64",
                    "@machine": "xenfy"
                }
            },
            "uuid": "5faa0019-4e84-4d57-8c9a-2c43d96819f3",
            "vcpu": {
                "#text": "2",
                "@placement": "static"
            }
        }
    }
]
```

####  Create

```POST /libvirt/xen/nodes/create```

Defines a domain, but does not start it. A previous definition for
this domain would be overridden if it already exists.

**Status Codes:**

- 201 - no error
- 404 - not found
- 406 - not acceptable
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/create HTTP/1.1
Content-Type: application/json

{
    "domain": {
        "@type": "xen",
        "clock": {
            "@offset": "utc"
        },
        "currentMemory": {
            "#text": "1048576",
            "@unit": "KiB"
        },
        "devices": {
            "console": {
                "@type": "pty",
                "target": {
                    "@port": "0",
                    "@type": "serial"
                }
            },
            "controller": [
                {
                    "@index": "0",
                    "@model": "ich9-ehci1",
                    "@type": "usb"
                },
                {
                    "@index": "0",
                    "@model": "ich9-ehci1",
                    "@type": "usb",
                    "master": {
                        "@startport": "0"
                    }
                }
            ],
            "disk": [
                {
                    "@device": "disk",
                    "@type": "file",
                    "address": {
                        "@bus": "1",
                        "@controller": "0",
                        "@target": "0",
                        "@type": "drive",
                        "@unit": "0"
                    },
                    "source": {
                        "@file": "/home/gemini/images/test0.raw"
                    },
                    "target": {
                        "@bus": "virtio",
                        "@dev": "hda"
                    }
                },
                {
                    "@device": "cdrom",
                    "@type": "file",
                    "address": {
                        "@bus": "1",
                        "@controller": "0",
                        "@target": "0",
                        "@type": "drive",
                        "@unit": "0"
                    },
                    "readonly": null,
                    "source": {
                        "@file": "/home/gemini/iso/CentOS-6.7-x86_64-minimal.iso"
                    },
                    "target": {
                        "@bus": "virtio",
                        "@dev": "hdc"
                    }
                }
            ],
            "emulator": "/usr/lib64/xen/bin/qemu-system-i386",
            "graphics": {
                "@autoport": "yes",
                "@listen": "0.0.0.0",
                "@port": "-1",
                "@type": "vnc",
                "listen": {
                    "@address": "0.0.0.0",
                    "@type": "address"
                }
            },
            "input": [
                {
                    "@bus": "usb",
                    "@type": "tablet"
                },
                {
                    "@bus": "ps2",
                    "@type": "mouse"
                },
                {
                    "@bus": "ps2",
                    "@type": "keyboard"
                }
            ],
            "interface": {
                "@type": "bridge",
                "mac": {
                    "@address": "00:16:3e:4d:87:7d"
                },
                "source": {
                    "@bridge": "ovs0"
                }
            },
            "serial": {
                "@type": "pty",
                "target": {
                    "@port": "0"
                }
            },
            "video": {
                "model": {
                    "@heads": "1",
                    "@type": "vga",
                    "@vram": "32768"
                }
            }
        },
        "features": {
            "acpi": null,
            "apic": null,
            "pae": null
        },
        "memory": {
            "#text": "1048576",
            "@unit": "KiB"
        },
        "name": "test0",
        "on_crash": "restart",
        "on_poweroff": "destroy",
        "on_reboot": "restart",
        "os": {
            "boot": [
                {
                    "@dev": "hd"
                },
                {
                    "@dev": "cdrom"
                }
            ],
            "loader": {
                "#text": "/usr/lib/xen/boot/hvmloader",
                "@type": "rom"
            },
            "type": {
                "#text": "hvm",
                "@arch": "x86_64",
                "@machine": "xenfy"
            }
        },
        "uuid": "5faa0019-4e84-4d57-8c9a-2c43d96819f3",
        "vcpu": {
            "#text": "2",
            "@placement": "static"
        }
    }
}
```

**Example response:**

```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "Uuid": "5faa0019-4e84-4d57-8c9a-2c43d96819f3",
    "Warnings": []
}
```

Json Parameters:

- TODO

#### Inspect

Provide an description of the domain. The description may be reused
later to relaunch the domain with Create request.

```GET /libvirt/xen/nodes/(id or name)/json```

Query Parameters:

- flag - 0/1/2/4/8. Default ```0```.

```
0 - VIR_DOMAIN_XML_DEFAULT
1 - VIR_DOMAIN_XML_SECURE
2 - VIR_DOMAIN_XML_INACTIVE
4 - VIR_DOMAIN_XML_UPDATE_CPU
8 - VIR_DOMAIN_XML_MIGRATABLE
```

**Status Codes:**

- 200 - no error
- 404 - no such domain
- 500 - server error

**Example request:**
```
GET /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/json HTTP/1.1
```

**Example response:**

```
{
    "domain": {
        "@type": "xen",
        "clock": {
            "@offset": "utc"
        },
        "currentMemory": {
            "#text": "1048576",
            "@unit": "KiB"
        },
        "devices": {
            "console": {
                "@type": "pty",
                "target": {
                    "@port": "0",
                    "@type": "serial"
                }
            },
            "controller": [
                {
                    "@index": "0",
                    "@model": "ich9-ehci1",
                    "@type": "usb"
                },
                {
                    "@index": "0",
                    "@model": "ich9-ehci1",
                    "@type": "usb",
                    "master": {
                        "@startport": "0"
                    }
                }
            ],
            "disk": [
                {
                    "@device": "disk",
                    "@type": "file",
                    "address": {
                        "@bus": "1",
                        "@controller": "0",
                        "@target": "0",
                        "@type": "drive",
                        "@unit": "0"
                    },
                    "source": {
                        "@file": "/home/gemini/images/test0.raw"
                    },
                    "target": {
                        "@bus": "virtio",
                        "@dev": "hda"
                    }
                },
                {
                    "@device": "cdrom",
                    "@type": "file",
                    "address": {
                        "@bus": "1",
                        "@controller": "0",
                        "@target": "0",
                        "@type": "drive",
                        "@unit": "0"
                    },
                    "readonly": null,
                    "source": {
                        "@file": "/home/gemini/iso/CentOS-6.7-x86_64-minimal.iso"
                    },
                    "target": {
                        "@bus": "virtio",
                        "@dev": "hdc"
                    }
                }
            ],
            "emulator": "/usr/lib64/xen/bin/qemu-system-i386",
            "graphics": {
                "@autoport": "yes",
                "@listen": "0.0.0.0",
                "@port": "-1",
                "@type": "vnc",
                "listen": {
                    "@address": "0.0.0.0",
                    "@type": "address"
                }
            },
            "input": [
                {
                    "@bus": "usb",
                    "@type": "tablet"
                },
                {
                    "@bus": "ps2",
                    "@type": "mouse"
                },
                {
                    "@bus": "ps2",
                    "@type": "keyboard"
                }
            ],
            "serial": {
                "@type": "pty",
                "target": {
                    "@port": "0"
                }
            },
            "video": {
                "model": {
                    "@heads": "1",
                    "@type": "vga",
                    "@vram": "32768"
                }
            }
        },
        "features": {
            "acpi": null,
            "apic": null,
            "pae": null
        },
        "memory": {
            "#text": "1048576",
            "@unit": "KiB"
        },
        "name": "test0",
        "on_crash": "restart",
        "on_poweroff": "destroy",
        "on_reboot": "restart",
        "os": {
            "boot": [
                {
                    "@dev": "hd"
                },
                {
                    "@dev": "cdrom"
                }
            ],
            "loader": {
                "#text": "/usr/lib/xen/boot/hvmloader",
                "@type": "rom"
            },
            "type": {
                "#text": "hvm",
                "@arch": "x86_64",
                "@machine": "xenfy"
            }
        },
        "uuid": "5faa0019-4e84-4d57-8c9a-2c43d96819f3",
        "vcpu": {
            "#text": "2",
            "@placement": "static"
        }
    }
}
```

#### Start

``` POST /libvirt/xen/nodes/(id or name)/start```

Launch a defined domain. If the call succeeds the domain moves from the
defined to the running domains pools.

Query Parameters:

- flag - 0/1/2/4/8/16. Default ```0```.

```
0 - VIR_DOMAIN_NONE
1 - VIR_DOMAIN_START_PAUSED
2 - VIR_DOMAIN_START_AUTODESTROY
4 - VIR_DOMAIN_START_BYPASS_CACHE
8 - VIR_DOMAIN_START_FORCE_BOOT
16 - VIR_DOMAIN_START_VALIDATE
```

**Status Codes:**

- 204 - no error
- 304 - domain already started
- 404 - no such domain
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/start HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Stop

```POST /libvirt/xen/nodes/(id or name)/stop```

Shutdown a domain, the domain object is still usable thereafter but
the domain OS is being stopped.

Query Parameters:

- flag - 0/1/2/4/8/16. Default ```0```.

```
0 - VIR_DOMAIN_SHUTDOWN_DEFAULT
1 - VIR_DOMAIN_SHUTDOWN_ACPI_POWER_BTN
2 - VIR_DOMAIN_SHUTDOWN_GUEST_AGENT
4 - VIR_DOMAIN_SHUTDOWN_INITCTL
8 - VIR_DOMAIN_SHUTDOWN_SIGNAL
16 - VIR_DOMAIN_SHUTDOWN_PARAVIRT
```

**Status Codes:**

- 204 - no error
- 304 - domain already stopped
- 404 - no such domain
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/stop HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Destroy

```POST /libvirt/xen/nodes/(id or name)/destroy```

Destroy the domain object. The running instance is shutdown if not down
already and all resources used by it are given back to the hypervisor.

Query Parameters:

- flag - 0/1. Default ```0```.

```
0 - VIR_DOMAIN_DESTROY_DEFAULT
1 - VIR_DOMAIN_DESTROY_GRACEFUL
```

**Status Codes:**

- 204 - no error
- 304 - domain already stopped
- 404 - no such domain
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/destroy HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Restart

```POST /libvirt/xen/nodes/(id or name)/restart```

Reboot a domain, the domain object is still usable thereafter, but the
domain OS is being stopped for a restart.

Query Parameters:

- flag - 0/1/2/4/8/16. Default ```0```.

```
0 - VIR_DOMAIN_REBOOT_DEFAULT
1 - VIR_DOMAIN_REBOOT_ACPI_POWER_BTN
2 - VIR_DOMAIN_REBOOT_GUEST_AGENT
4 - VIR_DOMAIN_REBOOT_INITCTL
8 - VIR_DOMAIN_REBOOT_SIGNAL
16 - VIR_DOMAIN_REBOOT_PARAVIRT
```

**Status Codes:**

- 204 - no error
- 404 - no such domain
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/restart HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Delete

```POST /libvirt/xen/nodes/(id or name)/delete```

Delete a domain. If the domain is running, it's converted to transient domain,
without stopping it. If the domain is inactive, the domain configuration
is removed.

Query Parameters:

- flag - 0/1/2/4. Default ```0```.

```
0 - VIR_DOMAIN_UNDEFINE_DEFAULT
1 - VIR_DOMAIN_UNDEFINE_MANAGED_SAVE
2 - VIR_DOMAIN_UNDEFINE_SNAPSHOTS_METADATA
4 - VIR_DOMAIN_UNDEFINE_NVRAM
```

**Status Codes:**

- 204 - no error
- 400 - bad parameter
- 404 - no such container
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/delete HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Suspend

```POST /libvirt/xen/nodes/(id or name)/suspend```

Suspends an active domain, the process is frozen without further access to CPU
resources and I/O but the memory used by the domain at the hypervisor level
will stay allocated.

**Status Codes:**

- 204 - no error
- 400 - bad parameter
- 404 - no such container
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/suspend HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Resume

```POST /libvirt/xen/nodes/(id or name)/resume```

Resume a suspended domain, the process is restarted from the state where it was
frozen by calling Suspend.

**Status Codes:**

- 204 - no error
- 400 - bad parameter
- 404 - no such container
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/resume HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Attach devices

```POST /libvirt/xen/nodes/(id or name)/devices/attach```

Attach a virtual device to a domain, using the flags parameter
to control how the device is attached.

Query Parameters:

- flag - 0/1/2. Default ```0```.

```
0 - VIR_DOMAIN_AFFECT_CURRENT
1 - VIR_DOMAIN_AFFECT_LIVE
2 - VIR_DOMAIN_AFFECT_CONFIG
```

**Status Codes:**

- 201 - no error
- 400 - bad parameter
- 404 - no such container
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/devices/attach HTTP/1.1
- TODO
```

**Example response:**

```
HTTP/1.1 201 Created
Content-Type: application/json

{
- TODO
}
```

Json Parameters:

- TODO

#### Resize memory

```POST /libvirt/xen/nodes/(id or name)/memory/resize```

Dynamically change the amount of physical memory allocated to a domain.

Query Parameters:

- size - size of memory to resize. The unit is KB.
- type - type of memory to resize.

```
max - Max memory
target - Target memory
```
- flag - 0/1/2. Default ```0```.

```
0 - VIR_DOMAIN_AFFECT_CURRENT
1 - VIR_DOMAIN_AFFECT_LIVE
2 - VIR_DOMAIN_AFFECT_CONFIG
```

**Status Codes:**

- 204 - no error
- 404 - no such domain
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/memory/resize?size=2097152&type=max&flag=0 HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

#### Resize VCPU

```POST /libvirt/xen/nodes/(id or name)/vcpu/resize```

Dynamically change the number of virtual CPUs used by the domain.

Query Parameters:

- size - size of VCPUs to resize.
- flag - 0/1/2. Default ```0```.

```
0 - VIR_DOMAIN_AFFECT_CURRENT
1 - VIR_DOMAIN_AFFECT_LIVE
2 - VIR_DOMAIN_AFFECT_CONFIG
```

**Status Codes:**

- 204 - no error
- 404 - no such domain
- 500 - server error

**Example request:**
```
POST /libvirt/xen/nodes/5faa0019-4e84-4d57-8c9a-2c43d96819f3/vcpu/resize?size=2&flag=0 HTTP/1.1
```

**Example response:**

```
HTTP/1.1 204 No Content
```

# Images
