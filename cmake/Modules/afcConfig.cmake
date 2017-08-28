INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_AFC afc)

FIND_PATH(
    AFC_INCLUDE_DIRS
    NAMES afc/api.h
    HINTS $ENV{AFC_DIR}/include
        ${PC_AFC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    AFC_LIBRARIES
    NAMES gnuradio-afc
    HINTS $ENV{AFC_DIR}/lib
        ${PC_AFC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(AFC DEFAULT_MSG AFC_LIBRARIES AFC_INCLUDE_DIRS)
MARK_AS_ADVANCED(AFC_LIBRARIES AFC_INCLUDE_DIRS)

