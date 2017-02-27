# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_xml_lite')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_xml_lite')
    _xml_lite = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_xml_lite', [dirname(__file__)])
        except ImportError:
            import _xml_lite
            return _xml_lite
        if fp is not None:
            try:
                _mod = imp.load_module('_xml_lite', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _xml_lite = swig_import_helper()
    del swig_import_helper
else:
    import _xml_lite
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class Element(_object):
    """Proxy of C++ xml::lite::Element class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Element, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _xml_lite.delete_Element
    __del__ = lambda self: None

    def destroyChildren(self):
        """destroyChildren(Element self)"""
        return _xml_lite.Element_destroyChildren(self)


    def __init__(self, *args):
        """
        __init__(xml::lite::Element self) -> Element
        __init__(xml::lite::Element self, std::string const & qname, std::string const & uri, std::string characterData) -> Element
        __init__(xml::lite::Element self, std::string const & qname, std::string const & uri) -> Element
        __init__(xml::lite::Element self, std::string const & qname) -> Element
        __init__(xml::lite::Element self, Element element) -> Element
        """
        this = _xml_lite.new_Element(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def clone(self, element):
        """clone(Element self, Element element)"""
        return _xml_lite.Element_clone(self, element)


    def attribute(self, s):
        """attribute(Element self, std::string const & s) -> std::string &"""
        return _xml_lite.Element_attribute(self, s)


    def getElementsByTagNameNS(self, *args):
        """
        getElementsByTagNameNS(Element self, std::string const & qname, std::vector< xml::lite::Element * > & elements, bool recurse=False)
        getElementsByTagNameNS(Element self, std::string const & qname, std::vector< xml::lite::Element * > & elements)
        getElementsByTagNameNS(Element self, std::string const & qname, bool recurse=False) -> std::vector< xml::lite::Element * >
        getElementsByTagNameNS(Element self, std::string const & qname) -> std::vector< xml::lite::Element * >
        """
        return _xml_lite.Element_getElementsByTagNameNS(self, *args)


    def getElementsByTagName(self, *args):
        """
        getElementsByTagName(Element self, std::string const & localName, std::vector< xml::lite::Element * > & elements, bool recurse=False)
        getElementsByTagName(Element self, std::string const & localName, std::vector< xml::lite::Element * > & elements)
        getElementsByTagName(Element self, std::string const & localName, bool recurse=False) -> std::vector< xml::lite::Element * >
        getElementsByTagName(Element self, std::string const & localName) -> std::vector< xml::lite::Element * >
        getElementsByTagName(Element self, std::string const & uri, std::string const & localName, std::vector< xml::lite::Element * > & elements, bool recurse=False)
        getElementsByTagName(Element self, std::string const & uri, std::string const & localName, std::vector< xml::lite::Element * > & elements)
        """
        return _xml_lite.Element_getElementsByTagName(self, *args)


    def setNamespacePrefix(self, prefix, uri):
        """setNamespacePrefix(Element self, std::string prefix, std::string uri)"""
        return _xml_lite.Element_setNamespacePrefix(self, prefix, uri)


    def setNamespaceURI(self, prefix, uri):
        """setNamespaceURI(Element self, std::string prefix, std::string uri)"""
        return _xml_lite.Element_setNamespaceURI(self, prefix, uri)


    def _print(self, stream):
        """_print(Element self, io::OutputStream & stream)"""
        return _xml_lite.Element__print(self, stream)


    def prettyPrint(self, *args):
        """
        prettyPrint(Element self, io::OutputStream & stream, std::string const & formatter)
        prettyPrint(Element self, io::OutputStream & stream)
        """
        return _xml_lite.Element_prettyPrint(self, *args)


    def hasElement(self, *args):
        """
        hasElement(Element self, std::string const & localName) -> bool
        hasElement(Element self, std::string const & uri, std::string const & localName) -> bool
        """
        return _xml_lite.Element_hasElement(self, *args)


    def getCharacterData(self):
        """getCharacterData(Element self) -> std::string"""
        return _xml_lite.Element_getCharacterData(self)


    def setCharacterData(self, characters):
        """setCharacterData(Element self, std::string const & characters)"""
        return _xml_lite.Element_setCharacterData(self, characters)


    def setLocalName(self, localName):
        """setLocalName(Element self, std::string const & localName)"""
        return _xml_lite.Element_setLocalName(self, localName)


    def getLocalName(self):
        """getLocalName(Element self) -> std::string"""
        return _xml_lite.Element_getLocalName(self)


    def setQName(self, qname):
        """setQName(Element self, std::string const & qname)"""
        return _xml_lite.Element_setQName(self, qname)


    def getQName(self):
        """getQName(Element self) -> std::string"""
        return _xml_lite.Element_getQName(self)


    def setUri(self, uri):
        """setUri(Element self, std::string const & uri)"""
        return _xml_lite.Element_setUri(self, uri)


    def getUri(self):
        """getUri(Element self) -> std::string"""
        return _xml_lite.Element_getUri(self)


    def getChildren(self, *args):
        """
        getChildren(Element self) -> std::vector< xml::lite::Element * >
        getChildren(Element self) -> std::vector< xml::lite::Element * > const &
        """
        return _xml_lite.Element_getChildren(self, *args)


    def getParent(self):
        """getParent(Element self) -> Element"""
        return _xml_lite.Element_getParent(self)


    def setParent(self, parent):
        """setParent(Element self, Element parent)"""
        return _xml_lite.Element_setParent(self, parent)

Element_swigregister = _xml_lite.Element_swigregister
Element_swigregister(Element)

class Document(_object):
    """Proxy of C++ xml::lite::Document class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Document, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Document, name)
    __repr__ = _swig_repr

    def __init__(self, rootNode=None, own=True):
        """
        __init__(xml::lite::Document self, Element rootNode=None, bool own=True) -> Document
        __init__(xml::lite::Document self, Element rootNode=None) -> Document
        __init__(xml::lite::Document self) -> Document
        """
        this = _xml_lite.new_Document(rootNode, own)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _xml_lite.delete_Document
    __del__ = lambda self: None

    def clone(self):
        """clone(Document self) -> Document"""
        return _xml_lite.Document_clone(self)


    def createElement(self, *args):
        """
        createElement(Document self, std::string const & qname, std::string const & uri, std::string characterData) -> Element
        createElement(Document self, std::string const & qname, std::string const & uri) -> Element
        """
        return _xml_lite.Document_createElement(self, *args)


    def destroy(self):
        """destroy(Document self)"""
        return _xml_lite.Document_destroy(self)


    def insert(self, element, underThis):
        """insert(Document self, Element element, Element underThis)"""
        return _xml_lite.Document_insert(self, element, underThis)


    def remove(self, *args):
        """
        remove(Document self, Element toDelete)
        remove(Document self, Element toDelete, Element fromHere)
        """
        return _xml_lite.Document_remove(self, *args)


    def setRootElement(self, element, own=True):
        """
        setRootElement(Document self, Element element, bool own=True)
        setRootElement(Document self, Element element)
        """
        return _xml_lite.Document_setRootElement(self, element, own)


    def getRootElement(self, *args):
        """
        getRootElement(Document self, bool steal=False) -> Element
        getRootElement(Document self) -> Element
        getRootElement(Document self) -> Element
        """
        return _xml_lite.Document_getRootElement(self, *args)

Document_swigregister = _xml_lite.Document_swigregister
Document_swigregister(Document)

class MinidomParser(_object):
    """Proxy of C++ xml::lite::MinidomParser class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MinidomParser, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MinidomParser, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(xml::lite::MinidomParser self) -> MinidomParser"""
        this = _xml_lite.new_MinidomParser()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _xml_lite.delete_MinidomParser
    __del__ = lambda self: None

    def parse(self, *args):
        """
        parse(MinidomParser self, io::InputStream & arg2, int size)
        parse(MinidomParser self, io::InputStream & arg2)
        """
        return _xml_lite.MinidomParser_parse(self, *args)


    def clear(self):
        """clear(MinidomParser self)"""
        return _xml_lite.MinidomParser_clear(self)


    def getDocument(self, *args):
        """
        getDocument(MinidomParser self) -> Document
        getDocument(MinidomParser self, bool steal=False) -> Document
        getDocument(MinidomParser self) -> Document
        """
        return _xml_lite.MinidomParser_getDocument(self, *args)


    def getReader(self, *args):
        """
        getReader(MinidomParser self) -> XMLReader const
        getReader(MinidomParser self) -> XMLReader &
        """
        return _xml_lite.MinidomParser_getReader(self, *args)


    def setDocument(self, newDocument, own=True):
        """
        setDocument(MinidomParser self, Document newDocument, bool own=True)
        setDocument(MinidomParser self, Document newDocument)
        """
        return _xml_lite.MinidomParser_setDocument(self, newDocument, own)


    def preserveCharacterData(self, preserve):
        """preserveCharacterData(MinidomParser self, bool preserve)"""
        return _xml_lite.MinidomParser_preserveCharacterData(self, preserve)

MinidomParser_swigregister = _xml_lite.MinidomParser_swigregister
MinidomParser_swigregister(MinidomParser)

# This file is compatible with both classic and new-style classes.


