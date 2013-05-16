/*
 * Copyright 2013 10gen Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


#include "mongoc-cluster-private.h"


void
mongoc_cluster_init (mongoc_cluster_t *cluster)
{
   bson_return_if_fail(cluster);
   memset(cluster, 0, sizeof *cluster);
}


void
mongoc_cluster_destroy (mongoc_cluster_t *cluster)
{
   bson_return_if_fail(cluster);

   /*
    * TODO: release resources.
    */
}


void
mongoc_cluster_seed (mongoc_cluster_t         *cluster,
                     const mongoc_host_list_t *from,
                     mongoc_stream_t          *from_stream,
                     const bson_t             *seed_info)
{
   bson_return_if_fail(cluster);
   bson_return_if_fail(from);
   bson_return_if_fail(from_stream);
   bson_return_if_fail(seed_info);

   /*
    * TODO: Add to list of members.
    */
}
