/* =========================================================================
 * This file is part of six.sicd-c++
 * =========================================================================
 *
 * (C) Copyright 2004 - 2014, MDA Information Systems LLC
 *
 * six.sicd-c++ is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this program; If not,
 * see <http://www.gnu.org/licenses/>.
 *
 */
#ifndef __SIX_COLLECTION_INFORMATION_H__
#define __SIX_COLLECTION_INFORMATION_H__

#include "six/Types.h"
#include "six/Init.h"
#include "six/Parameter.h"
#include "six/ParameterCollection.h"
#include "six/sicd/ComplexClassification.h"

namespace six
{
namespace sicd
{
/*!
 *  \struct CollectionInformation
 *  \brief SICD CollectionInfo parameter
 *
 *  Collection information used by SICD, representing the tag
 *  <CollectionInfo>.  This block contains general information about
 *  the collection.  There is nothing wrong with the SICD name, but
 *  for API consistency, naming is lengthened.  
 */
struct CollectionInformation
{

    /*!
     *  Radar platform identifier.  For bistatic
     *  collections, list the Receive platform
     */
    std::string collectorName;

    /*!
     *  (Optional) Radar platform identifier that provided
     *  the illumination.  For bistatic collections, list the 
     *  transmit platform.
     */
    std::string illuminatorName;

    /*!
     *  Collection & imaging data set identifier.  Uniquely identifies
     *  imaging collections per profile
     *
     */
    std::string coreName;

    /*!
     *  (Optional) Collection type identifier.  Monotstatic collections include
     *  single platform collections with unique transmit and receive apertures
     *  Allowed values are "MONOSTATIC" and "BISTATIC"
     *
     */
    CollectType collectType;

    /*!
     *  Radar Mode, must be SPOTLIGHT, STRIPMAP, or
     *  DYNAMIC_STRIPMAP
     *
     */
    RadarModeType radarMode;

    /*!
     *  (Optional) RadarMode ModeID.  Value dependent on profile
     */
    std::string radarModeID;

    /*!
     *  Classification.  File control & handling and any appropriate
     *  markings.  We attempt to map this to the SIDD controls.  If
     *  this does not work, the FileSecurity for a NITF can be retrieved
     *  from the NITFWriteControl or NITFReadControl
     */
    ComplexClassification classification;

    /*!
     *  (Optional)
     *  List of country codes for region covered by the image
     *
     */
    std::vector<std::string> countryCodes;

    /*!
     *  (Optional) Additional parameters
     */
    ParameterCollection parameters;

    //!  Constructor
    CollectionInformation();

    //!  Destructor
    ~CollectionInformation()
    {
    }

    //! Deep copy
    CollectionInformation* clone() const;

    bool operator==(const CollectionInformation& other) const
    {
        return collectorName == other.collectorName &&
               collectType == other.collectType &&
               illuminatorName == illuminatorName &&
               coreName == coreName &&
               radarMode == radarMode &&
               radarModeID == radarModeID;
    }

    bool operator!=(const CollectionInformation& other) const
    {
        return !((*this) == other);
    }
};

}
}
#endif

