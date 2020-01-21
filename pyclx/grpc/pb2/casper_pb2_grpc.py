# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import casper_pb2 as casper__pb2
from . import consensus_pb2 as consensus__pb2
from . import empty_pb2 as empty__pb2
from . import info_pb2 as info__pb2
from . import state_pb2 as state__pb2


class CasperServiceStub(object):
  """CasperService is the way for user and dApp developer to interact with the system,
  including deploying contracts, looking at the DAG and querying state.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Deploy = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/Deploy',
        request_serializer=casper__pb2.DeployRequest.SerializeToString,
        response_deserializer=empty__pb2.Empty.FromString,
        )
    self.GetBlockInfo = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/GetBlockInfo',
        request_serializer=casper__pb2.GetBlockInfoRequest.SerializeToString,
        response_deserializer=info__pb2.BlockInfo.FromString,
        )
    self.StreamBlockInfos = channel.unary_stream(
        '/io.casperlabs.node.api.casper.CasperService/StreamBlockInfos',
        request_serializer=casper__pb2.StreamBlockInfosRequest.SerializeToString,
        response_deserializer=info__pb2.BlockInfo.FromString,
        )
    self.GetDeployInfo = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/GetDeployInfo',
        request_serializer=casper__pb2.GetDeployInfoRequest.SerializeToString,
        response_deserializer=info__pb2.DeployInfo.FromString,
        )
    self.StreamBlockDeploys = channel.unary_stream(
        '/io.casperlabs.node.api.casper.CasperService/StreamBlockDeploys',
        request_serializer=casper__pb2.StreamBlockDeploysRequest.SerializeToString,
        response_deserializer=consensus__pb2.Block.ProcessedDeploy.FromString,
        )
    self.StreamEvents = channel.unary_stream(
        '/io.casperlabs.node.api.casper.CasperService/StreamEvents',
        request_serializer=casper__pb2.StreamEventsRequest.SerializeToString,
        response_deserializer=info__pb2.Event.FromString,
        )
    self.GetBlockState = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/GetBlockState',
        request_serializer=casper__pb2.GetBlockStateRequest.SerializeToString,
        response_deserializer=state__pb2.Value.FromString,
        )
    self.BatchGetBlockState = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/BatchGetBlockState',
        request_serializer=casper__pb2.BatchGetBlockStateRequest.SerializeToString,
        response_deserializer=casper__pb2.BatchGetBlockStateResponse.FromString,
        )
    self.ListDeployInfos = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/ListDeployInfos',
        request_serializer=casper__pb2.ListDeployInfosRequest.SerializeToString,
        response_deserializer=casper__pb2.ListDeployInfosResponse.FromString,
        )
    self.GetLastFinalizedBlockInfo = channel.unary_unary(
        '/io.casperlabs.node.api.casper.CasperService/GetLastFinalizedBlockInfo',
        request_serializer=casper__pb2.GetLastFinalizedBlockInfoRequest.SerializeToString,
        response_deserializer=info__pb2.BlockInfo.FromString,
        )


class CasperServiceServicer(object):
  """CasperService is the way for user and dApp developer to interact with the system,
  including deploying contracts, looking at the DAG and querying state.
  """

  def Deploy(self, request, context):
    """Add a deploy to the deploy pool on the node,
    to be processed during subsequent block proposals.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockInfo(self, request, context):
    """Get the block summary with extra information about finality.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamBlockInfos(self, request, context):
    """Get slices of the DAG, going backwards, rank by rank.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDeployInfo(self, request, context):
    """Retrieve information about a single deploy by hash.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamBlockDeploys(self, request, context):
    """Get the processed deploys within a block.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamEvents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockState(self, request, context):
    """Query the value of global state as it was after the execution of a block.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchGetBlockState(self, request, context):
    """Execute multiple state queries at once.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDeployInfos(self, request, context):
    """Get deploys list of a given account
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLastFinalizedBlockInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CasperServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Deploy': grpc.unary_unary_rpc_method_handler(
          servicer.Deploy,
          request_deserializer=casper__pb2.DeployRequest.FromString,
          response_serializer=empty__pb2.Empty.SerializeToString,
      ),
      'GetBlockInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockInfo,
          request_deserializer=casper__pb2.GetBlockInfoRequest.FromString,
          response_serializer=info__pb2.BlockInfo.SerializeToString,
      ),
      'StreamBlockInfos': grpc.unary_stream_rpc_method_handler(
          servicer.StreamBlockInfos,
          request_deserializer=casper__pb2.StreamBlockInfosRequest.FromString,
          response_serializer=info__pb2.BlockInfo.SerializeToString,
      ),
      'GetDeployInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetDeployInfo,
          request_deserializer=casper__pb2.GetDeployInfoRequest.FromString,
          response_serializer=info__pb2.DeployInfo.SerializeToString,
      ),
      'StreamBlockDeploys': grpc.unary_stream_rpc_method_handler(
          servicer.StreamBlockDeploys,
          request_deserializer=casper__pb2.StreamBlockDeploysRequest.FromString,
          response_serializer=consensus__pb2.Block.ProcessedDeploy.SerializeToString,
      ),
      'StreamEvents': grpc.unary_stream_rpc_method_handler(
          servicer.StreamEvents,
          request_deserializer=casper__pb2.StreamEventsRequest.FromString,
          response_serializer=info__pb2.Event.SerializeToString,
      ),
      'GetBlockState': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockState,
          request_deserializer=casper__pb2.GetBlockStateRequest.FromString,
          response_serializer=state__pb2.Value.SerializeToString,
      ),
      'BatchGetBlockState': grpc.unary_unary_rpc_method_handler(
          servicer.BatchGetBlockState,
          request_deserializer=casper__pb2.BatchGetBlockStateRequest.FromString,
          response_serializer=casper__pb2.BatchGetBlockStateResponse.SerializeToString,
      ),
      'ListDeployInfos': grpc.unary_unary_rpc_method_handler(
          servicer.ListDeployInfos,
          request_deserializer=casper__pb2.ListDeployInfosRequest.FromString,
          response_serializer=casper__pb2.ListDeployInfosResponse.SerializeToString,
      ),
      'GetLastFinalizedBlockInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetLastFinalizedBlockInfo,
          request_deserializer=casper__pb2.GetLastFinalizedBlockInfoRequest.FromString,
          response_serializer=info__pb2.BlockInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.casperlabs.node.api.casper.CasperService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
