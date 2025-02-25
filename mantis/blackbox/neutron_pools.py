# generated by datamodel-codegen:
#   filename:  neutron_pools.json

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Config(BaseModel):
    migrateToAddress: Optional[str] = None


class Prices(BaseModel):
    token1Address: str
    token1PriceUsd: float
    token2Address: str
    token2PriceUsd: float


class Asset(BaseModel):
    id: str
    address: str
    amount: str
    symbol: str


class AstroRewards(BaseModel):
    apr: float
    apy: float
    day: float


class ProtocolRewards(BaseModel):
    apr: float
    apy: float
    day: float


class TotalRewards(BaseModel):
    apr: Union[float, str]
    apy: int
    day: int


class TradingFees(BaseModel):
    apr: int
    apy: Union[float, str]
    day: float


class JsonItem(BaseModel):
    poolAddress: str
    lpAddress: str
    dayVolumeUsd: float
    poolLiquidityUsd: float
    poolLiquidity: int
    rewardTokenSymbol: Optional[str] = None
    config: Optional[Config] = None
    feeRate: List[str]
    poolType: str
    isBlocked: bool
    prices: Prices
    stakeable: bool
    assets: List[Asset]
    name: str
    isNew: bool
    isIlliquid: bool
    isDeregistered: bool
    sortingAssets: List[str]
    astroRewards: AstroRewards
    protocolRewards: ProtocolRewards
    totalRewards: TotalRewards
    tradingFees: TradingFees


class Model(BaseModel):
    json_: List[JsonItem] = Field(..., alias="json")
