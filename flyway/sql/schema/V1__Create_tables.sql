CREATE TABLE [dbo].[emp_master](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[emp_code] [varchar](20) NOT NULL,
	[emp_name] [varchar](100) NOT NULL,
	[emp_fathername] [varchar](100) NULL,
	[emp_sex] [char](1) NULL,
	[emp_dob] [date] NULL,
	[emp_doj] [date] NULL,
	[emp_doe] [date] NULL,
	[emp_presaddr] [varchar](255) NULL,
	[emp_premanaddr] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[emp_master]  WITH CHECK ADD CHECK  (([emp_sex]='F' OR [emp_sex]='M'))