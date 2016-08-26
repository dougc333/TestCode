/*
 * Copyright (C) 2012 Hernan Badino <hernan.badino@gmail.com>
 *
 * This file is part of QCV
 *
 * QCV is under the terms of the GNU Lesser General Public License
 * version 2.1. See the GNU LGPL version 2.1 for details.
 * QCV is distributed "AS IS" without ANY WARRANTY, without even the
 * implied warranty of merchantability or fitness for a particular
 * purpose. 
 *
 * In no event shall the authors or contributors be liable
 * for any direct, indirect, incidental, special, exemplary, or
 * consequential damages arising in any way out of the use of this
 * software.
 *
 * By downloading, copying, installing or using the software you agree
 * to this license. Do not download, install, copy or use the
 * software, if you do not agree to this license.
 */


#ifndef __DIRPATHPARAM_H
#define __DIRPATHPARAM_H

/*@@@**************************************************************************
 ** \dir  dirPathParam
 * \author Hernan Badino
 * \notes  
*******************************************************************************
*****             (C) Hernan Badino 2012 - All Rights Reserved            *****
******************************************************************************/

/* INCLUDES */
#include "stringParam.h"

namespace QCV
{
    /* PROTOTYPES */

    class CDirPathParameter : public CStringParameter
    {
    /// Constructors/Destructor
    public:
        /// Constructors/Destructor
        CDirPathParameter (  std::string               f_name_str = "",
                             std::string               f_comment_str = "",
                             std::string               f_value_str = "",
                             CParameterBaseConnector * f_connector_p = NULL );
        
    public:
        
        /// Get editor.
        virtual QWidget *       createEditor ( );
        
        /// Protected members
    protected:
        
    };
}


#endif // __STRINGPARAM_H
