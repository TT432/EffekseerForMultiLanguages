# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _EffekseerCore
else:
    import _EffekseerCore

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


EffekseerCoreDeviceType_Unknown = _EffekseerCore.EffekseerCoreDeviceType_Unknown
EffekseerCoreDeviceType_OpenGL = _EffekseerCore.EffekseerCoreDeviceType_OpenGL
class EffekseerBackendCore(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _EffekseerCore.EffekseerBackendCore_swiginit(self, _EffekseerCore.new_EffekseerBackendCore())
    __swig_destroy__ = _EffekseerCore.delete_EffekseerBackendCore

    @staticmethod
    def GetDevice():
        return _EffekseerCore.EffekseerBackendCore_GetDevice()

    @staticmethod
    def InitializeAsOpenGL():
        return _EffekseerCore.EffekseerBackendCore_InitializeAsOpenGL()

    @staticmethod
    def Terminate():
        return _EffekseerCore.EffekseerBackendCore_Terminate()

# Register EffekseerBackendCore in _EffekseerCore:
_EffekseerCore.EffekseerBackendCore_swigregister(EffekseerBackendCore)

def EffekseerBackendCore_GetDevice():
    return _EffekseerCore.EffekseerBackendCore_GetDevice()

def EffekseerBackendCore_InitializeAsOpenGL():
    return _EffekseerCore.EffekseerBackendCore_InitializeAsOpenGL()

def EffekseerBackendCore_Terminate():
    return _EffekseerCore.EffekseerBackendCore_Terminate()

EffekseerTextureType_Color = _EffekseerCore.EffekseerTextureType_Color
EffekseerTextureType_Normal = _EffekseerCore.EffekseerTextureType_Normal
EffekseerTextureType_Distortion = _EffekseerCore.EffekseerTextureType_Distortion
class EffekseerEffectCore(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _EffekseerCore.EffekseerEffectCore_swiginit(self, _EffekseerCore.new_EffekseerEffectCore())
    __swig_destroy__ = _EffekseerCore.delete_EffekseerEffectCore

    def Load(self, *args):
        return _EffekseerCore.EffekseerEffectCore_Load(self, *args)

    def GetTexturePath(self, index, type):
        return _EffekseerCore.EffekseerEffectCore_GetTexturePath(self, index, type)

    def GetTextureCount(self, type):
        return _EffekseerCore.EffekseerEffectCore_GetTextureCount(self, type)

    def LoadTexture(self, *args):
        return _EffekseerCore.EffekseerEffectCore_LoadTexture(self, *args)

    def HasTextureLoaded(self, index, type):
        return _EffekseerCore.EffekseerEffectCore_HasTextureLoaded(self, index, type)

    def GetModelPath(self, index):
        return _EffekseerCore.EffekseerEffectCore_GetModelPath(self, index)

    def GetModelCount(self):
        return _EffekseerCore.EffekseerEffectCore_GetModelCount(self)

    def LoadModel(self, *args):
        return _EffekseerCore.EffekseerEffectCore_LoadModel(self, *args)

    def HasModelLoaded(self, index):
        return _EffekseerCore.EffekseerEffectCore_HasModelLoaded(self, index)

    def GetMaterialPath(self, index):
        return _EffekseerCore.EffekseerEffectCore_GetMaterialPath(self, index)

    def GetMaterialCount(self):
        return _EffekseerCore.EffekseerEffectCore_GetMaterialCount(self)

    def LoadMaterial(self, *args):
        return _EffekseerCore.EffekseerEffectCore_LoadMaterial(self, *args)

    def HasMaterialLoaded(self, index):
        return _EffekseerCore.EffekseerEffectCore_HasMaterialLoaded(self, index)

# Register EffekseerEffectCore in _EffekseerCore:
_EffekseerCore.EffekseerEffectCore_swigregister(EffekseerEffectCore)

class EffekseerManagerCore(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _EffekseerCore.EffekseerManagerCore_swiginit(self, _EffekseerCore.new_EffekseerManagerCore())
    __swig_destroy__ = _EffekseerCore.delete_EffekseerManagerCore

    def Initialize(self, spriteMaxCount):
        return _EffekseerCore.EffekseerManagerCore_Initialize(self, spriteMaxCount)

    def Update(self, deltaFrames):
        return _EffekseerCore.EffekseerManagerCore_Update(self, deltaFrames)

    def BeginUpdate(self):
        return _EffekseerCore.EffekseerManagerCore_BeginUpdate(self)

    def EndUpdate(self):
        return _EffekseerCore.EffekseerManagerCore_EndUpdate(self)

    def UpdateHandleToMoveToFrame(self, handle, v):
        return _EffekseerCore.EffekseerManagerCore_UpdateHandleToMoveToFrame(self, handle, v)

    def Play(self, effect):
        return _EffekseerCore.EffekseerManagerCore_Play(self, effect)

    def Stop(self, handle):
        return _EffekseerCore.EffekseerManagerCore_Stop(self, handle)

    def SetPaused(self, handle, v):
        return _EffekseerCore.EffekseerManagerCore_SetPaused(self, handle, v)

    def SetShown(self, handle, v):
        return _EffekseerCore.EffekseerManagerCore_SetShown(self, handle, v)

    def SetEffectPosition(self, handle, x, y, z):
        return _EffekseerCore.EffekseerManagerCore_SetEffectPosition(self, handle, x, y, z)

    def SetEffectTransformMatrix(self, handle, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11):
        return _EffekseerCore.EffekseerManagerCore_SetEffectTransformMatrix(self, handle, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11)

    def DrawBack(self):
        return _EffekseerCore.EffekseerManagerCore_DrawBack(self)

    def DrawFront(self):
        return _EffekseerCore.EffekseerManagerCore_DrawFront(self)

    def SetProjectionMatrix(self, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15):
        return _EffekseerCore.EffekseerManagerCore_SetProjectionMatrix(self, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15)

    def SetCameraMatrix(self, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15):
        return _EffekseerCore.EffekseerManagerCore_SetCameraMatrix(self, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15)

    def Exists(self, handle):
        return _EffekseerCore.EffekseerManagerCore_Exists(self, handle)

    def SetViewProjectionMatrixWithSimpleWindow(self, windowWidth, windowHeight):
        return _EffekseerCore.EffekseerManagerCore_SetViewProjectionMatrixWithSimpleWindow(self, windowWidth, windowHeight)

    def SetDynamicInput(self, handle, index, value):
        return _EffekseerCore.EffekseerManagerCore_SetDynamicInput(self, handle, index, value)

    def GetDynamicInput(self, handle, index):
        return _EffekseerCore.EffekseerManagerCore_GetDynamicInput(self, handle, index)

    def LaunchWorkerThreads(self, n):
        return _EffekseerCore.EffekseerManagerCore_LaunchWorkerThreads(self, n)

# Register EffekseerManagerCore in _EffekseerCore:
_EffekseerCore.EffekseerManagerCore_swigregister(EffekseerManagerCore)


