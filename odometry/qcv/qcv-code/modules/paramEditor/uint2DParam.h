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


#ifndef __UINT2DPARAM_H
#define __UINT2DPARAM_H

/**
 *******************************************************************************
 *
 * @file uint2DParam.h
 *
 * \class CUInt2DParameter
 * \author Hernan Badino (hernan.badino@gmail.com)
 *
 * \brief Parameter interface for a S2D<unsigned int> variable.
 *
 * The class implements a parameter interface for a S2D<unsigned int> variable.
 *
 *******************************************************************************/

/* INCLUDES */
#include "parameter.h"
#include "standardTypes.h"

namespace QCV
{
    /* PROTOTYPES */

    class CUInt2DParameter : public CParameter
    {
    public:
        
        /// Constructors/Destructor
        CUInt2DParameter (  std::string               f_name_str = "",
                            std::string               f_comment_str = "",
                            S2D<unsigned int>         f_val = S2D<unsigned int>(0,0),
                            std::string               f_name1_str = "",
                            std::string               f_name2_str = "",
                            CParameterBaseConnector * f_connector_p = NULL );
        
        virtual ~CUInt2DParameter ();

    public:
        /// Get and set values from strings.
        virtual std::string     getStringFromValue ( ) const;
        virtual bool            setValueFromString ( std::string f_val_str );
 
        /// Get and set Int2D value
        virtual S2D<unsigned int> getValue ( ) const;
        virtual bool              setValue ( S2D<unsigned int> f_value,
                                             bool              f_shouldUpdate_b = true );
        
        const std::string *     getNames ( ) const 
        {
            return m_names_p;
        }

        /// Get editor.
        virtual QWidget *       createEditor ( );

    /// Protected members
    protected:

        /// Stored value.
        S2D<unsigned int>  m_value;

        /// Stored value.
        std::string  m_names_p[2];
    };
}


#endif // __UINT2DPARAM_H

