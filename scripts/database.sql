CREATE TABLE relation(
  id varchar(10),
  uid varchar(20),
  osm_user varchar(80),
  version integer,
  changeset varchar(20),
  osm_timestamp numeric,
  name varchar(200),  
  restriction varchar(50),
  type varchar(50)
  
)
--DROP TABLE relation
--DELETE from relation
--INSERT INTO relation(id, uid, osm_user, version, changeset, osm_timestamp, name, restriction, type)  VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s);
--select * from relation

CREATE TABLE fecha(
  id serial,
  s_date varchar(10),
  ts_date numeric 
)
ALTER TABLE fecha ADD COLUMN id serial;
--DROP TABLE fecha
--DELETE FROM fecha;
--INSERT INTO fecha(s_date, ts_date) VALUES (?, ?);
--select * from fecha

-- test
select count(*) from relation where 1293858000.0 < osm_timestamp and  osm_timestamp < 1296536400.0 and version =1
select count(*) from relation where 1293858000.0 < osm_timestamp and  osm_timestamp < 1296536400.0 and version >1

-- optener version =1
CREATE OR REPLACE FUNCTION get_version1 (id_start_month numeric) 
  RETURNS  int
  AS $$
DECLARE	
	_start_month numeric;
	_end_month numeric;
	_added int;
	BEGIN
		_start_month = (select ts_date from fecha where id=id_start_month);
		_end_month = (select ts_date from fecha where id=id_start_month+1);
		_added =(select count(*) from relation where _start_month < osm_timestamp and  osm_timestamp < _end_month and version =1);	
	RETURN _added;
	END;
$$ LANGUAGE plpgsql;

select get_version1( 1 );

-- optener version >1
CREATE OR REPLACE FUNCTION get_versionx (id_start_month numeric) 
  RETURNS  int
  AS $$
DECLARE	
	_start_month numeric;
	_end_month numeric;
	_edited int;
	BEGIN
		_start_month = (select ts_date from fecha where id=id_start_month);
		_end_month = (select ts_date from fecha where id=id_start_month+1);
		_edited =(select count(*) from relation where _start_month < osm_timestamp and  osm_timestamp < _end_month and version >1);	
	RETURN _edited;
	END;
$$ LANGUAGE plpgsql;

-- consulta
SELECT substring(s_date::text,4,9),get_version1(id) as added , get_versionx(id) as edited  FROM fecha;

select * from relation
select osm_user, count(version) as num_edit from relation GROUP BY osm_user ORDER BY  num_edit desc limit 20


select count(*) from relation








